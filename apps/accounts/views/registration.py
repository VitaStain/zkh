from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.accounts.models import Account
from apps.accounts.serializers.registration import AccountCreateSerializer

@extend_schema(tags=["authentication | registration"])
@extend_schema_view(
    post=extend_schema(
        summary="Регистрация пользователя по email",
    ),
)
class AccountProfileCreateView(generics.CreateAPIView):
    authentication_classes = []
    permission_classes = (~IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountCreateSerializer
