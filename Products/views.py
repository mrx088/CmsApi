from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductsSeralizer
from .models import Product

class AllProducts(APIView):
    def get(self,request):
        products = Product.objects.all()
        SrzData = ProductsSeralizer(instance=products,many=True)
        return Response(SrzData.data)