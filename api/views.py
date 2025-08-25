from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.utils.decorators import method_decorator
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from django.views import generic
from rest_framework.views import APIView
from api.authentications import TokenAuthentication
# If you have a PostStatus enum, import it
# from .models import PostStatus

# Create your views here.


class ProductAPIView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
ProductAPIView = ProductAPIView.as_view()