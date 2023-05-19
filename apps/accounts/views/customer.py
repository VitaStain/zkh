from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics, filters
from rest_framework.permissions import IsAdminUser

from apps.accounts.models import Account
from apps.accounts.serializers.customer import CustomerListSerializer
from zkh.docs import auto_docstring


@auto_docstring()
@extend_schema(
    tags=["customers"],
)
@extend_schema_view(
    get=extend_schema(
        summary="Получить список всех пользователей (для администраторов)",
    ),
)
class CustomerListView(generics.ListAPIView):
    queryset = Account.objects.filter(is_active=True, is_superuser=False)
    serializer_class = CustomerListSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend,
        filters.OrderingFilter,
    ]
    search_fields = ["id", "email"]
    ordering_fields = ["id", "email"]
