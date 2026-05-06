from ..models import OrganizerType

from .base_serializer import BaseSerializer


class OrganizerTypeSerializer(BaseSerializer):
    class Meta:
        model = OrganizerType
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
