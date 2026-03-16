from .base_repository import BaseRepository

from ..models import SponsorEveniment


class SponsorEvenimentRepository(BaseRepository):
    def __init__(self):
        super().__init__(SponsorEveniment)
