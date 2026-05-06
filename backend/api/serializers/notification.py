from ..models import Notification

from .base_serializer import BaseSerializer


class NotificationSerializer(BaseSerializer):
    class Meta:
        model = Notification
        fields = [
            "id",
            "user",
            "event",
            "notification_type",
            "title",
            "message",
            "scheduled_at",
            "sent_at",
            "is_read",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "sent_at", "created_at", "updated_at"]
