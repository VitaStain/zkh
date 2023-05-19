from rest_framework import serializers

from apps.accounts.serializers.customer import CustomerListSerializer
from apps.orders.models import Order
from apps.services.models import Service
from apps.services.serializers.service import ServiceSerializer
from zkh.exceptions import ServiceDoesNotExistException


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

    class Meta:
        model = Order
        fields = ("id", "customer", "service", "urgency", "time", "status")
