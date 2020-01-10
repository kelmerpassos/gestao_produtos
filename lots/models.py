from django.db import models

from products.models import Product


class InputLot(models.Model):
    number_input = models.IntegerField(unique=True)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.number_input)


class OutputLot(models.Model):
    number_output = models.IntegerField(unique=True)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.number_output)


