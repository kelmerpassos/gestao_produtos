from django.db import models
from providers.models import Provider


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.IntegerField(unique=True)
    provider = models.ForeignKey(Provider, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products_photos', blank=True, null=True)
    objects = models.Manager()
    def __str__(self):
        return self.name
