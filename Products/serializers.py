from rest_framework import serializers
from .models import Product


class ProductsSeralizer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'