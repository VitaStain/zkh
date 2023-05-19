from datetime import timedelta

from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

from apps.orders.models import Order
from apps.workers.models import Worker
from apps.workers.serializers.worker import WorkerSerializer
from zkh.docs import auto_docstring
from zkh.exceptions import OrderDoesNotExistException


@auto_docstring()
@extend_schema(
    tags=["workers"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Получить список всех мастеров (для администраторов)",
    ),
    post=extend_schema(
        summary="Создать мастера (для администраторов)",
    ),
)
class WorkerListCreateView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = WorkerSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["id", "name"]
    ordering_fields = ["id", "name"]
    filterset_fields = ("service",)


@auto_docstring()
@extend_schema(
    tags=["workers"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Получить детали мастера (для администраторов)",
    ),
    patch=extend_schema(
        summary="Изменить информацию о мастере (для администраторов)",
    ),
    delete=extend_schema(
        summary="Удалить мастера (для администраторов)",
    ),
)
class WorkerDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = WorkerSerializer
    http_method_names = ["get", "patch", "delete"]


@auto_docstring()
@extend_schema(
    tags=["workers"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Получить список всех свободных мастеров (для администраторов)",
        parameters=[
            OpenApiParameter(
                name="order_id",
                location=OpenApiParameter.QUERY,
                type=int,
                required=True,
                description="Заказ",
            ),
        ],
    ),
)
class WorkerFreeListView(generics.ListAPIView):
    permission_classes = (IsAdminUser,)
    serializer_class = WorkerSerializer

    def get_queryset(self):
        order_id = self.request.query_params.get("order_id", None)
        order = Order.objects.filter(id=order_id).first()
        if not order:
            raise OrderDoesNotExistException
        excludes_orders = Order.objects.filter(
            service=order.service,
            time__lte=order.time + timedelta(hours=1),
            time__gte=order.time - timedelta(hours=1),
        )
        workers = Worker.objects.filter(service=order.service).exclude(
            order__in=excludes_orders
        )

        return workers
