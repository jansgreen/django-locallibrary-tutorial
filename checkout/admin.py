from django.contrib import admin
from .models import order, OrderLineItem
# Register your models here.


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = (
        'lineitem_total',
        )

class OrderLineItem(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline, )
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        )

    fields = (
        'order_number',
        'date',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcade',
        'town_or_city',
        'street_address1',
        'street_address2',
        'delivery_cost',
        'order_total',
        'grand_total',
        )

    list_display = (
        'order_number',
        'date',
        'full_name',
        'delivery_cost',
        'order_total',
        'grand_total',
        )

    ordering = (
        '-date'
        )

admin.site.register(order, orderAdmin)
 