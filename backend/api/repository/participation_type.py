from .base_repository import BaseRepository

from domain.models import ParticipationType


class ParticipationTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(ParticipationType)
