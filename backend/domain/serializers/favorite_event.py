from ..models import FavoriteEvent
from .event import EventSerializer

from .base_serializer import BaseSerializer


class FavoriteEventSerializer(BaseSerializer):
    event = EventSerializer(read_only=True)

    class Meta:
        model = FavoriteEvent
        fields = ["id", "user", "event", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "event", "created_at", "updated_at"]
