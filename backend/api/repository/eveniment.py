from .base_repository import BaseRepository

from ..models import Eveniment


class EvenimentRepository(BaseRepository):
    def __init__(self):
        super().__init__(Eveniment)
