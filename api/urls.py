from . import views
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    path('auth/', obtain_auth_token, name='api-token-auth'),
    path('', views.ProductAPIView,name='product-api'),
]