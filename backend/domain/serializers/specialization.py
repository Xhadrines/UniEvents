from ..models import Specialization

from .base_serializer import BaseSerializer


class SpecializationSerializer(BaseSerializer):
    class Meta:
        model = Specialization
        fields = ["id", "name", "faculty", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
