from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.workers.models import Worker
from apps.workers.serializers.worker import WorkerSerializer
from zkh.docs import auto_docstring


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
