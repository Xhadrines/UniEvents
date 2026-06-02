from .base_service import BaseService

from ..repository import NotificationTypeRepository


class NotificationTypeService(BaseService):
    """
    Service responsabil pentru gestionarea tipurilor de notificări.

    Exemple:
    - notificare pentru eveniment nou,
    - reminder,
    - confirmare înscriere,
    - anulare eveniment.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu NotificationTypeRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul NotificationType.
        """

        super().__init__(NotificationTypeRepository())
