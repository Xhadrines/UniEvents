from .base_repository import BaseRepository

from ..models import NotificationType


class NotificationTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(NotificationType)
