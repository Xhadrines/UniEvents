from ..models import Role

from .base_serializer import BaseSerializer


class RoleSerializer(BaseSerializer):
    class Meta:
        model = Role
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
