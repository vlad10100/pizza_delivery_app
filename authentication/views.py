from rest_framework import status
from rest_framework.response import Response 
from rest_framework.views import APIView

from authentication.serializers import UserCreationSerializer

from drf_yasg.utils import swagger_auto_schema

class UserCreationView(APIView):
    serializer_class = UserCreationSerializer
    
    @swagger_auto_schema(operation_summary="CREATE User", request_body=serializer_class)
    def post(self, request):
        data = request.data 
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
