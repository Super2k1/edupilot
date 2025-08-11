from rest_framework import generics , mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import accounts
from .serializers import accountSerializer
from django.shortcuts import get_object_or_404
from django.views import generic
from rest_framework import status


class AccountCreateAPIView(generics.CreateAPIView):
    queryset = accounts.objects.all()
    serializer_class = accountSerializer
    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('category_type')
        if title is not None:
            serializer.validated_data['category_type'] = title.lower()
        serializer.save(category_type=title)

account_create_view = AccountCreateAPIView.as_view()


class AccountListAPIView(generics.ListAPIView):
        queryset = accounts.objects.all()
        serializer_class = accountSerializer


account_list_view = AccountListAPIView.as_view()

class AccountdetailAPIView(generics.RetrieveAPIView):
    queryset= accounts.objects.all()
    serializer_class = accountSerializer


account_detail_view = AccountdetailAPIView.as_view()


@api_view(['GET', 'POST'])
def account_alt_view(request, pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(accounts, pk=pk)
            data = accountSerializer(obj, many=False).data
            return Response(data)
        queryset = accounts.objects.all()
        data = accountSerializer(queryset, many=True).data
        return Response(data)

    if method == 'POST':
        serializer = accountSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('category_type')
            if title is not None:
                serializer.validated_data['category_type'] = title.lower()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountUpdateAPIView(generics.UpdateAPIView):
    queryset= accounts.objects.all()
    serializer_class = accountSerializer 
    lock_field = 'pk'
    def perform_update(self, serializer):
        title = serializer.validated_data.get('category_type')
        if title is not None:
            serializer.validated_data['category_type'] = title.lower()
        serializer.save()
account_update_view = AccountUpdateAPIView.as_view()

class AccountDestroyAPIView(generics.DestroyAPIView):
    queryset= accounts.objects.all()
    serializer_class = accountSerializer 
    lookup_field = 'pk'
    def perform_destroy(self, instance):
       return super().perform_destroy(instance)
    
    

account_delete_view = AccountDestroyAPIView.as_view()


class AccountsMixinView(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                         generics.GenericAPIView):
    queryset = accounts.objects.all()
    serializer_class = accountSerializer
    lookup_field = 'pk'

    def get(self,request,*args ,**kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        
        return self.list(request, *args, **kwargs)
    
account_mixin_view = AccountsMixinView.as_view()