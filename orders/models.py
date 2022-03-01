from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Order(models.Model):
    SIZE_CHOICES = (
        ('SMALL', 'SMALL'),
        ('MEDIUM', 'MEDIUM'),
        ('LARGE', 'LARGE'),
    )

    ORDER_STATUS = (
        ('PENDING', 'PENDING'),
        ('IN TRANSIT', 'IN TRANSIT'),
        ('DELIVERED', 'DELIVERED'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES, default=SIZE_CHOICES[0][0])    #SIZE_CHOICES[0][0] = SMALL
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS, default=ORDER_STATUS[0][0]) #ORDER_STATUS[0][0] = PENDING
    quantity = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        output = f"Order {self.size} -by {self.customer.id}"
        return output