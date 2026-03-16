from .base_repository import BaseRepository

from ..models import TipParticipare


class TipParticipareRepository(BaseRepository):
    def __init__(self):
        super().__init__(TipParticipare)
