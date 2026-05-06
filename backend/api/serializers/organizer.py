from ..models import Organizer

from .base_serializer import BaseSerializer


class OrganizerSerializer(BaseSerializer):
    class Meta:
        model = Organizer
        fields = [
            "id",
            "name",
            "description",
            "link",
            "organizer_type",
            "user",
            "status",
            "faculty",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
