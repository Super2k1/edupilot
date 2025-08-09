from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import accounts
from .serializers import accountSerializer


class AccountdetailAPIView(generics.RetrieveAPIView):
    queryset= accounts.objects.all()
    serializer_class = accountSerializer


account_list_view = AccountdetailAPIView.as_view()