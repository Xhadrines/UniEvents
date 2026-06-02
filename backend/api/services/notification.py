from django.utils import timezone

from .base_service import BaseService
from ..repository import NotificationRepository


class NotificationService(BaseService):
    """
    Service responsabil pentru gestionarea notificărilor.

    Acest service permite:
    - obținerea notificărilor utilizatorului,
    - filtrarea notificărilor necitite,
    - marcarea notificărilor ca citite,
    - crearea notificărilor noi.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu NotificationRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Notification.
        """

        super().__init__(NotificationRepository())

    def get_by_user(self, user_id: int):
        """
        Returnează toate notificările unui utilizator.
        """

        return self.repository.get_by_user(user_id)

    def get_unread_by_user(self, user_id: int):
        """
        Returnează doar notificările necitite
        ale utilizatorului.
        """

        return self.repository.get_unread_by_user(user_id)

    def mark_as_read(self, notification_id: int):
        """
        Marchează o notificare ca fiind citită.
        """

        return self.repository.mark_as_read(notification_id)

    def create_notification(
        self, user, title: str, message: str, notification_type, event=None
    ):
        """
        Creează o notificare nouă pentru utilizator.

        Parametri:
        - user -> utilizatorul care primește notificarea
        - title -> titlul notificării
        - message -> mesajul notificării
        - notification_type -> tipul notificării
        - event -> eveniment asociat notificării (opțional)
        """

        # Creăm notificarea în baza de date.
        return self.repository.create(
            user=user,
            title=title,
            message=message,
            notification_type=notification_type,
            event=event,
        )

    def mark_as_sent(self, notification_id: int):
        """
        Marchează notificarea ca fiind trimisă.

        Salvăm data și ora trimiterii în câmpul sent_at.
        """

        # Căutăm notificarea după ID.
        notification = self.repository.get_by_id(notification_id)

        # Dacă notificarea nu există, returnăm None.
        if not notification:
            return None

        # Salvăm momentul în care notificarea a fost trimisă.
        notification.sent_at = timezone.now()

        # Salvăm modificările în baza de date.
        notification.save()

        return notification
