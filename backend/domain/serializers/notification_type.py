from ..models import NotificationType

from .base_serializer import BaseSerializer


class NotificationTypeSerializer(BaseSerializer):
    class Meta:
        model = NotificationType
        fields = ["id", "name", "description", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
