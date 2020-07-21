from django.shortcuts import render
from rest_framework import viewsets
from .models import product , category,child_product
from .serialization import productSerializer ,categorySerializer,child_productSerializer

# # Create your views here.
# from empyloeeapi.serialization import productSerializer
# from empyloeeapi.models import product
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# @api_view(['GET'])
# def showproduct(request):
#     if request.method=='GET':
#         results=product.objects.all()
#         serialize=productSerializer(results,many=True)
#         return Response(serialize.data)

class productview(viewsets.ModelViewSet):
    queryset=product.objects.all()
    serializer_class=productSerializer

class categoryview(viewsets.ModelViewSet):
    queryset=category.objects.all()
    serializer_class=categorySerializer

class child_productview(viewsets.ModelViewSet):
    queryset=child_product.objects.all()
    serializer_class=child_productSerializer