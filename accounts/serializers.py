# from rest_framework import serializers
# from .models import account
# from rest_framework.reverse import reverse

# class accountSerializer(serializers.ModelSerializer):
#     url = serializers.SerializerMethodField(read_only=True)
#     email = serializers.EmailField(write_only=True)
#     class Meta:
#         model = account
#         fields = [
#             'url',
#             'pk',
#             'id',
#             'email',
#             'category_type',
#             'actif',
#         ]
#     # def validate_category_type(self, value):
#     #     qs = accounts.objects.filter(category_type__iexact=value)
#     #     if self.instance:
#     #         qs = qs.exclude(pk=self.instance.pk)
#     #     if qs.exists():
#     #         raise serializers.ValidationError(f"{value} is already a category type")
#     #     return value

#     """def create(self , validated_data):
#         email = validated_data.pop('email')
#         obj =  super().create(validated_data)
#         #print(email,obj)
#         return obj
#     def update(self,instance,validated_data):
#         email = validated_data.pop('email',None)
#         return super().update(instance,validated_data)"""
#     def get_url(self, obj):
#         #return f"/api/accounts/{obj.pk}/"
#         request = self.context.get('request')
#         if request is None:
#             return None
#         return reverse("account-detail",kwargs={"pk":obj.pk},request = request,)