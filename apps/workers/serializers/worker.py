from rest_framework import serializers

from apps.services.serializers.service import ServiceSerializer
from apps.workers.models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=True)

    class Meta:
        model = Worker
        fields = ("id", "name", "service")
