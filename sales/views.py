from django.shortcuts import render
from rest_framework import generics
from .models import Product, Sale
from .serializers import ProductSerializer, SaleSerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleListCreate(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
