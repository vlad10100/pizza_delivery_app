from rest_framework import serializers

from orders.models import Order 
from authentication.models import User


class OrderCreationSerializer(serializers.ModelSerializer):
    order_status = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = ['id', 'size', 'order_status', 'quantity', 'customer']



class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        exclude = ['order_status']



class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order 
        fields = ['id', 'order_status', 'customer']



class UserOrderListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['order_status', 'size', 'quantity']



class UserOrdersSerializer(serializers.ModelSerializer):
    orders = UserOrderListSerializer(many=True, read_only=True, source='order_set')     # source = Order object === order_set
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'phone_number', 'orders']

