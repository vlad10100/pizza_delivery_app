from django.urls import path 

from orders.views import OrdersAPI

app_name='orders'

urlpatterns = [
    path('', OrdersAPI.as_view(), name='orders-api')
]
