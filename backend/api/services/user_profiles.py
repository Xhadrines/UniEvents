from .base_service import BaseService

from ..repository import UserProfilesRepository


class UserProfilesService(BaseService):
    def __init__(self):
        super().__init__(UserProfilesRepository())

    def get_by_user_id(self, user_id):
        return self.repository.get_by_user_id(user_id)
