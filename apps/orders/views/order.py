from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from apps.orders.models import Order, OrderStatus
from apps.orders.serializers.order import (
    OrderCreateSerializer,
    OrderListSerializer,
    OrderDetailSerializer,
    OrderUpdateSerializer,
)
from zkh.docs import auto_docstring


@auto_docstring()
@extend_schema(
    tags=["orders"],
)
@extend_schema_view(
    post=extend_schema(
        summary="Создать заказ (для пользователей)",
    ),
)
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = OrderCreateSerializer


@auto_docstring()
@extend_schema(
    tags=["orders"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Посмотреть список заказов (для администратора)",
    ),
)
class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = OrderListSerializer
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_fields = ("status",)


@auto_docstring()
@extend_schema(
    tags=["orders"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Посмотреть детали заказов (для администратора)",
    ),
)
class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = OrderDetailSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.status == OrderStatus.NEW:
            obj.status = OrderStatus.VIEWED
            obj.save()
        return obj


@extend_schema(
    tags=["orders"],
)
@extend_schema_view(
    patch=extend_schema(
        summary="Добавить мастера к заказу (для администратора)",
    ),
)
class OrderUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = OrderUpdateSerializer
    http_method_names = ["patch"]
