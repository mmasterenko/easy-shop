from django.contrib.auth import get_user_model
from rest_framework import serializers

from apps.shop import models as shop_models


User = get_user_model()


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = shop_models.Product
        fields = [
            'id',
            'title',
            'text',
        ]
