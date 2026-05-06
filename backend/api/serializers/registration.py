from ..models import Registration

from .base_serializer import BaseSerializer


class RegistrationSerializer(BaseSerializer):
    class Meta:
        model = Registration
        fields = [
            "id",
            "user",
            "event",
            "status",
            "confirmation_email_sent",
            "ticket_qr_code",
            "checked_in",
            "checked_in_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
