from ..models import Location

from .base_serializer import BaseSerializer


class LocationSerializer(BaseSerializer):
    class Meta:
        model = Location
        fields = [
            "id",
            "name",
            "address",
            "building",
            "room",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
