from rest_framework import serializers

from ..models import Rol


class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ["id", "nume", "descriere", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
