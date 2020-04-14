from django.db import models

from Users.models import user
from books.models import Proposed_Book

# Create your models here.


class Cart(models.Model):
    #date_created = models.DateTimeField(auto_now_add=True , null=True, blank=True )
    created_by = models.ForeignKey(user, null=True, blank=True, on_delete=models.CASCADE)
    order_items = models.ManyToManyField(Proposed_Book , related_name= 'Item_want_to_buy')






#auto_now_add=True, null=True, blank=True
# class Product(models.Model):
#     product = models.OneToOneField(Proposed_Book, related_name="Item_order", on_delete=models.SET_NULL, null=True)
#     #date_created = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=255)
#     #product_name = models.CharField(max_length=255)
#     original_price = models.DecimalField(max_digits=10, decimal_places=2)
#     our_price = models.DecimalField(max_digits=10, decimal_places=2)
#     origianl_url = models.TextField()
#     image_url = models.TextField()
#     html = models.TextField()
#     options = models.TextField()
#     imageData = models.TextField()

# class OrderItem(models.Model):
#     product = models.OneToOneField(Proposed_Book ,related_name="Item_order", on_delete=models.SET_NULL, null=True)
#     is_ordered = models.BooleanField(default=False)
#     date_added = models.DateTimeField(auto_now=True)
#     date_ordered = models.DateTimeField(null=True)
#
#     # def __str__(self):
#     #     return self.product.name
#
#
# class Order(models.Model):
#     ref_code = models.CharField(max_length=15)
#     owner_want_to_buy = models.ForeignKey(user, on_delete=models.SET_NULL, null=True)
#     is_ordered = models.BooleanField(default=False)
#     items = models.ManyToManyField(OrderItem)
#     date_ordered = models.DateTimeField(auto_now=True)
#
#     def get_cart_items(self):
#         return self.items.all()
#
#     def get_cart_total(self):
#         return sum([item.product.Offered_price for item in self.items.all()])
#
#     def __str__(self):
#         return '{0} - {1}'.format(self.owner, self.ref_code)
#
#
# class Transaction(models.Model):
#     profile = models.ForeignKey(user, on_delete=models.CASCADE)
#     #token = models.CharField(max_length=120)
#     order_id = models.CharField(max_length=120)
#     amount = models.DecimalField(max_digits=100, decimal_places=2)
#     success = models.BooleanField(default=True)
#     timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
#
#     def __str__(self):
#         return self.order_id
#
#     class Meta:
#         ordering = ['-timestamp']
#


