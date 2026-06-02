from .base_repository import BaseRepository

from domain.models import Location


class LocationRepository(BaseRepository):
    """
    Repository responsabil pentru operațiile legate de locații.

    Acest repository moștenește toate metodele CRUD
    din BaseRepository și le aplică modelului Location.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Location.

        Astfel, toate operațiile efectuate prin acest repository
        vor lucra pe tabela Location.
        """

        super().__init__(Location)
