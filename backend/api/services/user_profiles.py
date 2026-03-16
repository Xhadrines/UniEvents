from .base_service import BaseService

from ..repository import UserProfilesRepository


class UserProfilesService(BaseService):
    def __init__(self):
        super().__init__(UserProfilesRepository())
