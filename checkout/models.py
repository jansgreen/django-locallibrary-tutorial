import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from catalog.models import Movies


# Create your models here.
class order(models.Model):
    order_number = models.CharField(max_length=20, null=True, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_numeber = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcade =models.CharField(max_length=20, null=True, blank=True)
    town_or_city =models.CharField(max_length=40, null=False, blank=False)
    street_address1 =models.CharField(max_length=80, null=False, blank=False)
    street_address2 =models.CharField(max_length=80, null=True, blank=True)
    country = models.CharField(max_length=80, null=True, blank=True)
    date =models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False default=0)



    def _generate_order_number(self):
        """ generate a random, unique order number using UUID  """

        return uuid.uuid4().hex.upper()

    def update_total():
        """ update grand total each time a line item is added"""

        self.order_total = self.lineitem_total.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ override the original  save method to set the order number if it hasn't set already"""
        if not self.order_number:
            self.order_number = self. _generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    order = models.ForeignKey(order, null=False, blank=False, on_delete= models.CASCADE, related_name='lineitems')
    Movie = models.ForeignKey(Movie, null=False, blank=False, on_delete= models.CASCADE)
    quantity = models.IntegerField(null = False, blank=False, default=0)
    lineitem_total = models.DateField(max_digits = 6, decimal_places = 2, null = False, blank=False, editable=False)

    def save(self, *args, **kwargs):
    """ override the original  save method to set the order number if it hasn't set already"""
        self.lineitem_total = self.Movie.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.Movie.id}'
