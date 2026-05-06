from .base_service import BaseService

from ..repository import FavoriteEventRepository


class FavoriteEventService(BaseService):
    def __init__(self):
        super().__init__(FavoriteEventRepository())

    def get_by_user(self, user_id: int):
        return self.repository.get_by_user(user_id)

    def add_to_favorites(self, user, event):
        # Adauga evenimentul la favorite daca nu exista deja
        favorite = self.repository.get_by_user_and_event(user.id, event.id)

        if favorite:
            return favorite

        return self.repository.create(user=user, event=event)

    def remove_from_favorites(self, user_id: int, event_id: int):
        # Sterge evenimentul din favorite
        favorite = self.repository.get_by_user_and_event(user_id, event_id)

        if not favorite:
            return False

        favorite.delete()
        return True
