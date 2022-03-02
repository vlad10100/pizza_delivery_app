from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status

from orders.models import Order
from orders.serializers import OrderCreationSerializer, OrderDetailSerializer, OrderStatusSerializer, UserOrdersSerializer

from authentication.models import User


from drf_yasg.utils import swagger_auto_schema



class OrderCreationView(APIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticated]


    @swagger_auto_schema(operation_summary="Get all orders")
    def get(self, request, format=None):
        order = Order.objects.all()
        serializer = self.serializer_class(instance=order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(operation_summary="Create an order", request_body=serializer_class)
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        
        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class OrderDetailView(APIView):
    serializer_class = OrderDetailSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]


    @swagger_auto_schema(operation_summary="Get order's details")
    def get(self, request, order_id, format=None):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(operation_summary="Update order's detail", request_body=serializer_class)
    def put(self, request, order_id, format=None):
        data = request.data 
        order = get_object_or_404(Order, id=order_id)
        serializer = self.serializer_class(instance=order, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_summary="Delete order")
    def delete(self, request, order_id, format=None):
        order = get_object_or_404(Order, pk=order_id)
        if order:
            order.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderStatusView(APIView):
    serializer_class= OrderStatusSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]


    @swagger_auto_schema(operation_summary="View an order's status")
    def get(self, request, order_id, format=None):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    @swagger_auto_schema(operation_summary="Update an order's status", request_body=serializer_class)
    def put(self, request, order_id, format=None):
        data = request.data
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class UserOrderListView(APIView):
    serializer_class = UserOrdersSerializer
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly]

    @swagger_auto_schema(operation_summary="View orders made by user")
    def get(self, request, format=None, **kwargs):
        user = User.objects.get(pk=kwargs['user_id'])
        serializer = self.serializer_class(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)