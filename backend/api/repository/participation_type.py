from .base_repository import BaseRepository

from domain.models import ParticipationType


class ParticipationTypeRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea tipurilor de participare.

    Exemple:
    - online,
    - fizic,
    - hibrid.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul ParticipationType.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela ParticipationType.
        """

        super().__init__(ParticipationType)
