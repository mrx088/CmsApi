from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductsSeralizer
from .models import Product
from django.shortcuts import get_object_or_404
from django.utils.text import slugify
from rest_framework import status

class AllProducts(APIView):
    def get(self,request):
        products = Product.objects.all()
        SrzData = ProductsSeralizer(instance=products,many=True)
        return Response(SrzData.data)
    
class EditProduct(APIView):
    def put(self,request,pk):
        print('RESEVE REQ')
        product = get_object_or_404(Product,pk=pk)
        SrzData = ProductsSeralizer(data=request.data,instance=product,partial=True)
        if SrzData.is_valid():
            print('OK')
            cd = SrzData.validated_data
            product.slug = slugify(cd['title'])
            product.save()
            SrzData.save()
            return Response(SrzData.data,status=status.HTTP_200_OK)
        return Response(SrzData.errors,status=status.HTTP_400_BAD_REQUEST)
