from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    """Данные токена"""

    refresh = serializers.CharField()
    access_token = serializers.CharField()
