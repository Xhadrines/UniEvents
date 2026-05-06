from django.utils import timezone

from .base_service import BaseService
from ..repository import NotificationRepository


class NotificationService(BaseService):
    def __init__(self):
        super().__init__(NotificationRepository())

    def get_by_user(self, user_id: int):
        return self.repository.get_by_user(user_id)

    def get_unread_by_user(self, user_id: int):
        return self.repository.get_unread_by_user(user_id)

    def mark_as_read(self, notification_id: int):
        return self.repository.mark_as_read(notification_id)

    def create_notification(
        self, user, title: str, message: str, notification_type, event=None
    ):
        # Creeaza o notificare simpla pentru utilizator
        return self.repository.create(
            user=user,
            title=title,
            message=message,
            notification_type=notification_type,
            event=event,
        )

    def mark_as_sent(self, notification_id: int):
        # Marcheaza notificarea ca trimisa
        notification = self.repository.get_by_id(notification_id)

        if not notification:
            return None

        notification.sent_at = timezone.now()
        notification.save()

        return notification
