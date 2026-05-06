from .base_repository import BaseRepository

from ..models import FavoriteEvent


class FavoriteEventRepository(BaseRepository):
    def __init__(self):
        super().__init__(FavoriteEvent)

    def get_by_user(self, user_id: int):
        # Returneaza evenimentele favorite ale unui utilizator
        return self.model.objects.filter(user_id=user_id)

    def get_by_user_and_event(self, user_id: int, event_id: int):
        # Returneaza un eveniment favorit specific
        return self.model.objects.filter(user_id=user_id, event_id=event_id).first()
