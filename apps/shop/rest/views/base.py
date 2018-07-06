from rest_framework.generics import ListCreateAPIView

from utils.rest_framework.generics import RetrieveUpdateDestroy
from apps.shop import models as shop_models
from apps.shop.rest import serializers as shop_serializers


class ProductListView(ListCreateAPIView):
    serializer_class = shop_serializers.ProductSerializer

    def get_queryset(self):
        return shop_models.Product.objects.filter(is_archive=False)


class ProductDetailView(RetrieveUpdateDestroy):
    serializer_class = shop_serializers.ProductSerializer

    def get_queryset(self):
        return shop_models.Product.objects.filter(is_archive=False)
