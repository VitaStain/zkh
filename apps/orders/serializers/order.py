from rest_framework import serializers

from apps.accounts.serializers.customer import CustomerListSerializer
from apps.orders.models import Order, OrderStatus
from apps.services.models import Service
from apps.services.serializers.service import ServiceSerializer
from apps.workers.models import Worker
from apps.workers.serializers.worker import WorkerSerializer
from zkh.exceptions import ServiceDoesNotExistException, WorkerDoesNotExistException


class OrderCreateSerializer(serializers.ModelSerializer):
    service_id = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ("service_id", "urgency", "time")

    def validate_service_id(self, value):
        if not Service.objects.filter(id=value):
            raise ServiceDoesNotExistException
        return value

    def create(self, validated_data):
        service_id = validated_data.pop("service_id")
        urgency = validated_data.pop("urgency")
        time = validated_data.pop("time")
        customer = self.context["request"].user
        order = Order.objects.create(
            customer=customer, service_id=service_id, urgency=urgency, time=time
        )
        return order


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("id", "customer", "service", "urgency", "time", "status")


class OrderDetailSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    customer = CustomerListSerializer()
    worker = WorkerSerializer()

    class Meta:
        model = Order
        fields = ("id", "customer", "service", "urgency", "time", "status", "worker")


class OrderUpdateSerializer(serializers.ModelSerializer):
    worker_id = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ("id", "worker_id")

    def validate_worker_id(self, value):
        if not Worker.objects.filter(id=value):
            raise WorkerDoesNotExistException
        return value

    def update(self, instance, validated_data):
        instance.worker_id = validated_data["worker_id"]
        instance.status = OrderStatus.PROCESSED
        instance.save()
        return instance
