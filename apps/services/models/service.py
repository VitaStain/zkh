from django.db import models


class Service(models.Model):
    title = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
