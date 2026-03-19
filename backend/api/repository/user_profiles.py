from .base_repository import BaseRepository

from ..models import UserProfiles


class UserProfilesRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProfiles)

    def get_by_user_id(self, user_id):
        return self.model.objects.filter(user_id=user_id).first()
