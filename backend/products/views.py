from rest_framework import generics
from rest_framework.response import Response
from products.serializers import ProductSerializers
from products.models import Product

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)
        # return super().perform_create(serializer)


product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView): # Single model/instance view
    queryset = Product.objects.all()
    serializer_class = ProductSerializers # Serializing the queryset