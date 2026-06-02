from .base_repository import BaseRepository

from domain.models import NotificationType


class NotificationTypeRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea tipurilor de notificări.

    Exemple:
    - notificare pentru eveniment nou,
    - reminder,
    - confirmare înscriere,
    - anulare eveniment.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul NotificationType.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela NotificationType.
        """

        super().__init__(NotificationType)
