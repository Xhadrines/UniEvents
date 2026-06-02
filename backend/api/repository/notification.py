from .base_repository import BaseRepository

from domain.models import Notification


class NotificationRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea notificărilor.

    Acest repository permite:
    - obținerea notificărilor unui utilizator,
    - filtrarea notificărilor necitite,
    - marcarea notificărilor ca citite.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Notification.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela Notification.
        """

        super().__init__(Notification)

    def get_by_user(self, user_id: int):
        """
        Returnează toate notificările unui utilizator.

        order_by("-created_at"):
        - sortează notificările descrescător după data creării
        - cele mai noi notificări apar primele
        """

        return self.model.objects.filter(user_id=user_id).order_by("-created_at")

    def get_unread_by_user(self, user_id: int):
        """
        Returnează doar notificările necitite ale utilizatorului.

        is_read=False înseamnă:
        - notificarea nu a fost încă deschisă/citită.
        """

        return self.model.objects.filter(user_id=user_id, is_read=False)

    def mark_as_read(self, notification_id: int):
        """
        Marchează o notificare ca fiind citită.

        Practic:
        - schimbăm câmpul is_read din False în True.
        """

        # Căutăm notificarea după ID.
        notification = self.get_by_id(notification_id)

        # Dacă notificarea nu există, returnăm None.
        if not notification:
            return None

        # Marcăm notificarea ca fiind citită.
        notification.is_read = True

        # Salvăm modificarea în baza de date.
        notification.save()

        return notification
