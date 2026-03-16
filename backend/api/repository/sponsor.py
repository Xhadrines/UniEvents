from .base_repository import BaseRepository

from ..models import Sponsor


class SponsorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Sponsor)
