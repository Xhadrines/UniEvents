from ..models import ParticipationType

from .base_serializer import BaseSerializer


class ParticipationTypeSerializer(BaseSerializer):
    class Meta:
        model = ParticipationType
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
