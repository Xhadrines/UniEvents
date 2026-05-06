from .base_repository import BaseRepository

from domain.models import Sponsor


class SponsorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Sponsor)
