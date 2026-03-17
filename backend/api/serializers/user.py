from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "last_name",
            "first_name",
            "is_superuser",
            "is_staff",
            "is_active",
            "last_login",
            "date_joined",
        ]
        read_only_fields = ["id", "date_joined", "last_login"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"required": False},
            "is_staff": {"required": False},
            "is_active": {"required": False},
        }
