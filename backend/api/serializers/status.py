from ..models import Status

from .base_serializer import BaseSerializer


class StatusSerializer(BaseSerializer):
    class Meta:
        model = Status
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
