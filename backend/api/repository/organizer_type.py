from .base_repository import BaseRepository

from ..models import OrganizerType


class OrganizerTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(OrganizerType)
