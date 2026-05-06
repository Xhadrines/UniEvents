from .base_repository import BaseRepository

from domain.models import Specialization


class SpecializationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Specialization)
