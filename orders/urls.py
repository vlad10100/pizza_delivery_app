from django.urls import path 

from orders.views import OrderCreationView, OrderDetailView, OrderStatusView, UserOrderListView

app_name='orders'

urlpatterns = [
    path('', OrderCreationView.as_view(), name='order-creation'),
    path('detail/<int:order_id>/', OrderDetailView.as_view(), name='order-detail'),
    path('status/<int:order_id>/', OrderStatusView.as_view(), name='order-status'),
    path('user/<int:user_id>/', UserOrderListView.as_view(), name='user-orders'),
]
