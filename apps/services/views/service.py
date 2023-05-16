from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser, AllowAny

from apps.services.models import Service
from apps.services.serializers.service import ServiceSerializer
from zkh.docs import auto_docstring


@auto_docstring()
@extend_schema(
    tags=["services"],
)
@extend_schema_view(
    post=extend_schema(
        summary="Создать услугу (для администраторов)",
    )
)
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    permission_classes = (IsAdminUser,)
    serializer_class = ServiceSerializer


@auto_docstring()
@extend_schema(
    tags=["services"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Получить все услуги (для всех типов пользователей)",
    )
)
class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ServiceSerializer
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["id", "title"]
    ordering_fields = ["id", "title", "price"]


@auto_docstring()
@extend_schema(
    tags=["services"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Получить детали услуги (для всех типов пользователей)",
    ),
    patch=extend_schema(
        summary="Изменить услугу (для администраторов)",
    ),
    delete=extend_schema(
        summary="Удалить услугу (для администраторов)",
    ),
)
class ServiceDetailPatchDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    http_method_names = ["get", "patch", "delete"]

    def get_permissions(self):
        if self.request.method == "GET":
            permission_classes = (AllowAny,)
        else:
            permission_classes = (IsAdminUser,)
        return [permission() for permission in permission_classes]
