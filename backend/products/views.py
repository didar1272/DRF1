from rest_framework import generics
from rest_framework.response import Response
from products.serializers import ProductSerializers
from products.models import Product



class ProductDetailAPIView(generics.RetrieveAPIView): # Single model/instance view
    queryset = Product.objects.all()
    serializer_class = ProductSerializers # Serializing the queryset