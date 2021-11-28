from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BaseAbstractModel(models.Model):
    # Ever created save create time Every model created I need modified and create time.
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    modified_at = models.DateTimeField(verbose_name="Mpdified at", auto_now=True)

    class Meta:
        abstract = True
