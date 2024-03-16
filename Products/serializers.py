from rest_framework import serializers
from .models import Product


class ProductsSeralizer(serializers.ModelSerializer):
    image = serializers.ImageField(read_only=True)
    class Meta :
        model = Product
        exclude = ('created',)
