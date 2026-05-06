from ..models import Faculty

from .base_serializer import BaseSerializer


class FacultySerializer(BaseSerializer):
    class Meta:
        model = Faculty
        fields = ["id", "name", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
