from django.db import models

from products import enums


class ProductQuerySet(models.QuerySet):
    def query(self):
        return super().query().filter(is_deleted=False)
    # stogu 10 adetten buyuk fiyati 100 dusuk olan urunler
    def banner_products(self):
        return self.filter(stock__quantity__gte=10, price__amount__lt=100)

    def has_stock(self):
        return self.filter(stock__quantity__gt=0)

    def create_product(self, name, size, sku, color):
        if self.filter(color=enums.Colors.RED).count() < 10:
            return self.create(name=name, color=color, size=size, sku=sku)
        return ValueError()
