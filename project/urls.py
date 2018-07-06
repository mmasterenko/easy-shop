from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_urls')),
]

if settings.DEBUG:
    import debug_toolbar
    from rest_framework.documentation import include_docs_urls
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="Swagger UI 3.0 | ReDoc",
            default_version='v1',
            description="Test description",
            # terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="mmasterenko@gmail.com"),
            # license=openapi.License(name="BSD License"),
        ),
        validators=['flex', 'ssv'],
        public=True,
        permission_classes=(permissions.AllowAny,),
    )

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('admin/docs/admin-doc', include('django.contrib.admindocs.urls')),
        path('api-docs/builtin', include_docs_urls(title='Built-in API', authentication_classes=[],
                                                   permission_classes=[])),
        re_path(r'^api-docs/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None),
                name='schema-json'),
        path('api-docs/swagger', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
        path('api-docs/redoc', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc'),
    ] + urlpatterns
