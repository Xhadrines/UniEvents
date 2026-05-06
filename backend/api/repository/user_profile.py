from .base_repository import BaseRepository

from domain.models import UserProfile


class UserProfileRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProfile)

    def get_by_user(self, user_id: int):
        # Returneaza profilul unui utilizator
        return self.model.objects.filter(user_id=user_id).first()

    def get_by_user_id(self, user_id: int):
        return self.get_by_user(user_id)
