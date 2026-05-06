from ..models import EmailToken

from .base_serializer import BaseSerializer


class EmailTokenSerializer(BaseSerializer):
    class Meta:
        model = EmailToken
        fields = [
            "id",
            "user",
            "token",
            "is_used",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "token", "created_at", "updated_at"]
