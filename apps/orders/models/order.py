from django.db import models

from apps.accounts.models import Account
from apps.services.models import Service


class Urgency(models.TextChoices):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Order(models.Model):
    customer = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="order"
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="order")
    urgency = models.CharField(max_length=50, choices=Urgency.choices)
    time = models.DateTimeField()

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
