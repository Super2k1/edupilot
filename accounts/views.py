from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import accounts
from .serializers import accountSerializer

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    instance = accounts.objects.all().order_by('?').first()
    data = {}
    if instance:
        serializer = accountSerializer(instance)
        return Response(serializer.data)
    return Response({"message": "No data available"})

# Create your views here.
