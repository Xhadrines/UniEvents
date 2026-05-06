from ..models import EventSponsor

from .base_serializer import BaseSerializer


class EventSponsorSerializer(BaseSerializer):
    class Meta:
        model = EventSponsor
        fields = ["id", "sponsor", "event", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
