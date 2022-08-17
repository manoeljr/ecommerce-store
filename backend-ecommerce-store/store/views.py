from django.shortcuts import render

from rest_framework import generics

from store.models import Product
from store.models import Category
from store.serializers import ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class Product(generics.RetrieveAPIView):
    lookup_field = 'slug'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryItemView(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])
