from django.db import models

from apps.accounts.models import Account
from apps.services.models import Service
from apps.workers.models import Worker


class OrderStatus(models.TextChoices):
    NEW = "new"
    VIEWED = "viewed"
    PROCESSED = "processed"


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
    status = models.CharField(
        max_length=50, choices=OrderStatus.choices, default=OrderStatus.NEW
    )
    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name="worker",
        null=True,
        blank=True,
        default="",
    )
    time = models.DateTimeField()

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
