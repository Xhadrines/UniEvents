from .base_repository import BaseRepository

from ..models import ParticipationType


class ParticipationTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(ParticipationType)
