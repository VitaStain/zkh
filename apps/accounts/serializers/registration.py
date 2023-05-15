from django.contrib.auth.password_validation import validate_password
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
)

from apps.accounts.models import Account
from apps.accounts.serializers.token import TokenSerializer
from zkh.exceptions import EmailAlreadyExistsException, PasswordsDoNotMatchException


class AccountCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    password_confirmation = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Account
        fields = (
            "username",
            "password",
            "password_confirmation",
            "email",
            "token",
        )

    def validate_email(self, value):
        if Account.objects.filter(email=value).exists():
            raise EmailAlreadyExistsException
        return value

    def validate(self, attrs):

        validate_password(password=attrs["password"])

        if attrs["password"] != attrs["password_confirmation"]:
            raise PasswordsDoNotMatchException

        return attrs

    def validate_password(self, value):
        validate_password(value)
        return value

    def create(self, validated_data):
        account = Account.objects.create_user(
            email=validated_data["email"], username=validated_data["username"]
        )
        account.set_password(validated_data["password"])
        account.is_active = True
        account.save()
        return account

    @extend_schema_field(TokenSerializer)
    def get_token(self, instance):
        token = TokenObtainPairSerializer.get_token(instance)
        result = {"refresh": token, "access_token": token.access_token}
        return TokenSerializer(result).data
