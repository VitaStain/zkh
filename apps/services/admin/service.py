from django.contrib import admin

from apps.orders.models import Order


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ("id", "urgency", "time")
    raw_id_fields = (
        "customer",
        "service",
    )
