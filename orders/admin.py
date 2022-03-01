from django.contrib import admin

from orders.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ['created_at', 'updated_at']
    list_display = ['customer', 'size', 'order_status', 'quantity']
    list_filter = ['created_at', 'order_status', 'size']