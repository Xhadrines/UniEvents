from rest_framework import serializers

from ..models import Registration

from .base_serializer import BaseSerializer


class RegistrationSerializer(BaseSerializer):
    status_name = serializers.CharField(source="status.name", read_only=True)

    class Meta:
        model = Registration
        fields = [
            "id",
            "user",
            "event",
            "status",
            "status_name",
            "confirmation_email_sent",
            "ticket_qr_code",
            "checked_in",
            "checked_in_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
