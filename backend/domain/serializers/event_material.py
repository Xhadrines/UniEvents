from ..models import EventMaterial

from .base_serializer import BaseSerializer


class EventMaterialSerializer(BaseSerializer):
    class Meta:
        model = EventMaterial
        fields = [
            "id",
            "event",
            "material_type",
            "title",
            "file",
            "is_public",
            "uploaded_by",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
