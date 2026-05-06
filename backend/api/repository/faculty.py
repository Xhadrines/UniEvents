from .base_repository import BaseRepository

from domain.models import Faculty


class FacultyRepository(BaseRepository):
    def __init__(self):
        super().__init__(Faculty)
