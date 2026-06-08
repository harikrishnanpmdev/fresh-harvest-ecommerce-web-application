from django.db import models
from shop.models import Product
from django.contrib.auth.models import User

class Cart(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=0)
    date_added= models.DateTimeField(auto_now_add=True)

    def subtotal(self):
        return self.product.price*self.quantity

    def __str__(self):
        return self.product.name
    
class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    order_amount= models.DecimalField(max_digits=10, decimal_places=2, null=True)
    order_id= models.CharField(max_length=50, null=True)
    ordered_date= models.DateTimeField(auto_now_add=True)
    payment_method= models.CharField(max_length=60, null=True)
    address= models.TextField(null=True)
    phone= models.CharField(max_length=15, null=True)
    is_ordered= models.BooleanField(default=False)
    delivery_status= models.CharField(default="Pending", max_length=60, null=True)

    def __str__(self):
        return str(self.order_id)
    
class OrderItems(models.Model):
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    order= models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity= models.IntegerField(default=0)

    def __str__(self):
        return str(self.order.order_id)