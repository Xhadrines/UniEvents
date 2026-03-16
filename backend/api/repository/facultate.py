from .base_repository import BaseRepository

from ..models import Facultate


class FacultateRepository(BaseRepository):
    def __init__(self):
        super().__init__(Facultate)
