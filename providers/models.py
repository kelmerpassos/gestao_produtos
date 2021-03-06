from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(unique=True, max_length=17)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return self.name
