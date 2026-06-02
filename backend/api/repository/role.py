from .base_repository import BaseRepository

from domain.models import Role


class RoleRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea rolurilor utilizatorilor.

    Exemple de roluri:
    - ADMIN,
    - STUDENT,
    - ORGANIZER,
    - MODERATOR.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Role.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela Role.
        """

        super().__init__(Role)
