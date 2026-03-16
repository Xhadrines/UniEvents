from .base_repository import BaseRepository

from ..models import Specializare


class SpecializareRepository(BaseRepository):
    def __init__(self):
        super().__init__(Specializare)
