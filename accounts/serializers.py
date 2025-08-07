from rest_framework import serializers
from .models import accounts


class accountSerializer(serializers.ModelSerializer):
    class Meta:
        model = accounts
        fields = [
            'id',
            'category_type',
            'actif',
        ]