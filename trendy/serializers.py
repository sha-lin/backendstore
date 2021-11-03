
from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator



class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = ['title', 'price', 'category', 'description', 'image']