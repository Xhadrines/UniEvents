from .base_repository import BaseRepository

from domain.models import NotificationType


class NotificationTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(NotificationType)
