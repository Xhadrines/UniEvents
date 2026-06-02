from .base_repository import BaseRepository

from domain.models import Status


class StatusRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea statusurilor.

    Exemple de statusuri:
    - Acceptat,
    - Respins,
    - În așteptare,
    - Finalizat.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Status.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela Status.
        """

        super().__init__(Status)
