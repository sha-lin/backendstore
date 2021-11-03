from django.contrib.auth.models import User
from authentication.models import User
from .serializers import  ProductSerializer
from .models import Product, Cart, Category
from rest_framework import generics, status, serializers, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsStaffPermission
from rest_framework.exceptions import NotFound

from django.shortcuts import redirect



class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated, IsStaffPermission]
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'message': f"Product {serializer.data['title']} has been created"}, status=status.HTTP_201_CREATED)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    lookup_url_kwargs = 'product_id'

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return Product.objects.filter(pk=product_id)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        if len(serializer.data):
            [response] = serializer.data
        else:
            raise NotFound('The product is not found',
                           code='product_not_found')

        return Response(response, status=status.HTTP_200_OK)