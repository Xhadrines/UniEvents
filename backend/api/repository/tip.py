from .base_repository import BaseRepository

from ..models import Tip


class TipRepository(BaseRepository):
    def __init__(self):
        super().__init__(Tip)
