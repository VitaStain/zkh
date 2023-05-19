from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import Order
from apps.orders.serializers.order import OrderCreateSerializer
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
