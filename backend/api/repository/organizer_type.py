from .base_repository import BaseRepository

from domain.models import OrganizerType


class OrganizerTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(OrganizerType)
