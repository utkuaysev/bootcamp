from django.contrib import admin

from orders.forms import OrderAdminForm
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Inline for Order Item
    """
    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin View for Order
    """
    list_display = ('customer', 'basket', 'total_price')
    list_filter = ('customer', )
    inlines = (OrderItemInline, )
    form = OrderAdminForm


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin View for OrderItem
    """
    list_display = ('order', 'product', 'price')
