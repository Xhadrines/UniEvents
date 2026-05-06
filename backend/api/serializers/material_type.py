from ..models import MaterialType

from .base_serializer import BaseSerializer


class MaterialTypeSerializer(BaseSerializer):
    class Meta:
        model = MaterialType
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
