from .base_repository import BaseRepository

from domain.models import Organizer


class OrganizerRepository(BaseRepository):
    """
    Repository responsabil pentru operațiile legate de organizatori.

    Organizatorii pot reprezenta:
    - facultăți,
    - companii,
    - organizații,
    - persoane sau grupuri care creează evenimente.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Organizer.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela Organizer.
        """

        super().__init__(Organizer)
