from .base_repository import BaseRepository

from ..models import Locatie


class LocatieRepository(BaseRepository):
    def __init__(self):
        super().__init__(Locatie)
