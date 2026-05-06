from ..models import Sponsor

from .base_serializer import BaseSerializer


class SponsorSerializer(BaseSerializer):
    class Meta:
        model = Sponsor
        fields = [
            "id",
            "name",
            "description",
            "link",
            "logo",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
