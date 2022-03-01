from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from orders.models import Order
from orders.serializers import OrderCreationSerializer, OrderDetailSerializer, OrderStatusSerializer, UserOrderListSerializer

from authentication.models import User

class OrderCreationView(APIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()
    permission_classes = [IsAuthenticated]


    def post(self, request, format=None):
        data = request.data
        serializer = self.serializer_class(data=data)
        
        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        order = Order.objects.all()
        serializer = self.serializer_class(instance=order, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class OrderDetailView(APIView):
    serializer_class = OrderDetailSerializer

    def get(self, request, order_id, format=None):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id, format=None):
        data = request.data 
        order = get_object_or_404(Order, id=order_id)
        serializer = self.serializer_class(instance=order, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id, format=None):
        order = get_object_or_404(Order, pk=order_id)
        if order:
            order.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderStatusView(APIView):
    serializer_class= OrderStatusSerializer

    def get(self, request, order_id, format=None):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id, format=None):
        data = request.data
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order, data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserOrderListView(APIView):
    serializer_class = UserOrderListSerializer
    # serializer_class = OrderDetailSerializer

    def get(self, request, format=None, **kwargs):
        user = User.objects.get(pk=kwargs['user_id'])
        orders = Order.objects.filter(customer=user)
        serializer = self.serializer_class(instance=orders, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)