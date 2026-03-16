from .base_repository import BaseRepository

from ..models import Inregistrare


class InregistrareRepository(BaseRepository):
    def __init__(self):
        super().__init__(Inregistrare)
