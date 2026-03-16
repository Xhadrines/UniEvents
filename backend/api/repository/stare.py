from .base_repository import BaseRepository

from ..models import Stare


class StareRepository(BaseRepository):
    def __init__(self):
        super().__init__(Stare)
