from rest_framework import serializers

from store.models import Product
from store.models import ProductImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image', 'alt_text']


class ProductSerializer(serializers.ModelSerializer):
    product_image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'category', 'title', 'description', 'slug', 'regular_price', 'product_image']
