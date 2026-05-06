from .base_repository import BaseRepository

from ..models import Organizer


class OrganizerRepository(BaseRepository):
    def __init__(self):
        super().__init__(Organizer)
