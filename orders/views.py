from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

class OrdersAPI(APIView):
    def get(self, request, format=None):
        return Response(data={"Message":"Orders API"}, status=status.HTTP_200_OK)