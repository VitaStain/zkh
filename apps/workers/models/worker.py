from django.db import models

from apps.services.models import Service


class Worker(models.Model):
    name = models.CharField(max_length=255)
    service = models.ManyToManyField(
        Service,
        related_name="worker",
        blank=True,
        verbose_name="Услуга",
    )

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"
