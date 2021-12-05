from django import forms
from django.core.exceptions import ValidationError

from orders.models import Order


class OrderAdminForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("customer", "basket", "status", "shipping_address", "billing_address")

    def clean(self):
        cleaned_data = super().clean()
        # import ipdb;ipdb.set_trace()
        ship = cleaned_data.get("shipping_address")
        customer = cleaned_data.get("customer")
        if not customer.address_set.filter(id=ship.id).exists():
            raise ValidationError(
                message={"shipping_address": _("Shipping address must be customer address")}
            )
        if cleaned_data.get("total_price") and cleaned_data.get("total_price") < 10:
            raise ValidationError(message={"total_price": _("Total must be greater than 10")})
        return cleaned_data
