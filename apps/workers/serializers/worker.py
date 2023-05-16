from rest_framework import serializers

from apps.workers.models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ("id", "name", "service")
