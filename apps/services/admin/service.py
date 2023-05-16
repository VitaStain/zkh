from django.contrib import admin

from apps.services.models import Service


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ("title", "price")
