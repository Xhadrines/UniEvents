from .base_repository import BaseRepository

from ..models import Notification


class NotificationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Notification)

    def get_by_user(self, user_id: int):
        # Returneaza notificarile unui utilizator
        return self.model.objects.filter(user_id=user_id).order_by("-created_at")

    def get_unread_by_user(self, user_id: int):
        # Returneaza notificarile necitite ale unui utilizator
        return self.model.objects.filter(user_id=user_id, is_read=False)

    def mark_as_read(self, notification_id: int):
        # Marcheaza o notificare ca citita
        notification = self.get_by_id(notification_id)

        if not notification:
            return None

        notification.is_read = True
        notification.save()
        return notification
