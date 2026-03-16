from .base_repository import BaseRepository

from ..models import UserProfiles


class UserProfilesRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProfiles)
