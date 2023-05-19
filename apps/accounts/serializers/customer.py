from rest_framework import serializers

from apps.accounts.models import Account


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("id", "username", "email")
