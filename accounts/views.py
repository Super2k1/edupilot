# from rest_framework import generics , mixins 
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from .models import account
# from .serializers import accountSerializer
# from django.shortcuts import get_object_or_404
# from rest_framework import status
# from api.mixins import StaffEditorPermissionMixin



# class AccountCreateAPIView(StaffEditorPermissionMixin , generics.CreateAPIView):
#     queryset = account.objects.all()
#     serializer_class = accountSerializer
#     def perform_create(self, serializer):
#         #serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('category_type')
#         if title is not None:
#             serializer.validated_data['category_type'] = title.lower()
#         serializer.save(category_type=title)

# account_create_view = AccountCreateAPIView.as_view()


# class AccountListAPIView(StaffEditorPermissionMixin,generics.ListAPIView):
#     queryset = account.objects.all()
#     serializer_class = accountSerializer
#     def get_queryset(self):
#         # Log the auth headers for debugging
#         print(f"Auth Headers: {self.request.headers.get('Authorization')}")
#         return super().get_queryset()

# account_list_view = AccountListAPIView.as_view()

# class AccountdetailAPIView(StaffEditorPermissionMixin ,generics.RetrieveAPIView):
#     queryset= account.objects.all()
#     serializer_class = accountSerializer


# account_detail_view = AccountdetailAPIView.as_view()


# @api_view(['GET', 'POST'])
# def account_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == 'GET':
#         if pk is not None:
#             obj = get_object_or_404(account, pk=pk)
#             data = accountSerializer(obj, many=False).data
#             return Response(data)
#         queryset = account.objects.all()
#         data = accountSerializer(queryset, many=True).data
#         return Response(data)

#     if method == 'POST':
#         serializer = accountSerializer(data=request.data)
#         if serializer.is_valid():
#             title = serializer.validated_data.get('category_type')
#             if title is not None:
#                 serializer.validated_data['category_type'] = title.lower()
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AccountUpdateAPIView(StaffEditorPermissionMixin,generics.UpdateAPIView):
#     queryset= account.objects.all()
#     serializer_class = accountSerializer 
#     lock_field = 'pk'
#     def perform_update(self, serializer):
#         title = serializer.validated_data.get('category_type')
#         if title is not None:
#             serializer.validated_data['category_type'] = title.lower()
#         serializer.save()
# account_update_view = AccountUpdateAPIView.as_view()

# class AccountDestroyAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
#     queryset= account.objects.all()
#     serializer_class = accountSerializer 
#     lookup_field = 'pk'
#     def perform_destroy(self, instance):
#        return super().perform_destroy(instance)
    
    

# account_delete_view = AccountDestroyAPIView.as_view()


# class AccountsMixinView(mixins.ListModelMixin,
#                         mixins.CreateModelMixin,
#                         mixins.RetrieveModelMixin,
#                         generics.GenericAPIView):
    
#     queryset = account.objects.all()
#     serializer_class = accountSerializer
#     lookup_field = 'pk'

#     def get(self,request,*args ,**kwargs):
#         print(args, kwargs)
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
        
#         return self.list(request, *args, **kwargs)
    
#     def post(self,request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def perform_create(self, serializer):
#         #serializer.save(user=self.request.user)
#         print(serializer.validated_data)
#         category_type = serializer.validated_data.get('category_type') or None
#         if category_type is not None:
#             category_type = category_type.lower()
#             print("this is cool view making a post request", category_type)
#         serializer.save(category_type=category_type)
    
# account_mixin_view = AccountsMixinView.as_view()