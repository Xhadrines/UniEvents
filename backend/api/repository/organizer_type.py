from .base_repository import BaseRepository

from domain.models import OrganizerType


class OrganizerTypeRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea tipurilor de organizatori.

    Exemple:
    - facultate,
    - companie,
    - organizație,
    - asociație studențească.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul OrganizerType.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela OrganizerType.
        """

        super().__init__(OrganizerType)
