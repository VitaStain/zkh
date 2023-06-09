from django.contrib import admin

from apps.workers.models.worker import Worker


@admin.register(Worker)
class AdminWorker(admin.ModelAdmin):
    list_display = ("id", "name",)
    raw_id_fields = ("service",)
