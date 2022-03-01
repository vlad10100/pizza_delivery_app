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




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'username', 'email', 'phone_number',]



class UserOrderListSerializer(serializers.ModelSerializer):
    # orders_made = OrderDetailSerializer(many=True, read_only=True)
    # customer = UserSerializer(many=True, read_only=True)
    orders_made = OrderDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ['customer', 'orders_made', 'order_status', 'size', 'quantity']
