from .base_repository import BaseRepository

from domain.models import Faculty


class FacultyRepository(BaseRepository):
    """
    Repository responsabil pentru operațiile legate de facultăți.

    Acest repository moștenește toate metodele CRUD
    din BaseRepository:
    - creare,
    - citire,
    - actualizare,
    - ștergere.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Faculty.

        Astfel, toate metodele din BaseRepository
        vor opera pe tabela Faculty.
        """

        super().__init__(Faculty)
