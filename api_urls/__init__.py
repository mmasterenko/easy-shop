from django.http import HttpResponse
from django.urls import path

from apps.shop.rest import views as shop_views


app_name = 'api'

urlpatterns = [
    # account and users
    path('user/<int:pk>', lambda r: HttpResponse('OK'), name='user-detail'),
    path('user',          lambda r: HttpResponse('OK'), name='user-list'),

    # shop
    path('product/<int:pk>', shop_views.ProductDetailView.as_view(), name='product-detail'),
    path('product',          shop_views.ProductListView.as_view(), name='product-list'),
]
