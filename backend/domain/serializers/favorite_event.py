from ..models import FavoriteEvent

from .base_serializer import BaseSerializer


class FavoriteEventSerializer(BaseSerializer):
    class Meta:
        model = FavoriteEvent
        fields = ["id", "user", "event", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
