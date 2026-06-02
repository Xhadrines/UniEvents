from django.utils import timezone

from .utils import aware
from api.repository import (
    UserRepository,
    EventRepository,
    NotificationTypeRepository,
)


def default_notification_data():
    """
    Returnează datele default pentru notificări.

    Aceste notificări sunt utilizate pentru:
    - remindere evenimente,
    - confirmări înscriere,
    - testare,
    - seed-ul inițial al bazei de date.
    """

    # =====================================================
    # REPOSITORIES
    # =====================================================

    user_repository = UserRepository()

    event_repository = EventRepository()

    notification_type_repository = NotificationTypeRepository()

    # =====================================================
    # USER + EVENT
    # =====================================================

    # Utilizator demo.
    student = user_repository.get_instance_by_username("student")

    # Eveniment pentru reminder.
    event = event_repository.get_instance_by_name("Targ de Cariere USV 2026")

    return [
        # =====================================================
        # EVENT REMINDER
        # =====================================================
        {
            # Utilizatorul care primește notificarea.
            "user": student,
            # Eveniment asociat notificării.
            "event": event,
            # Tip notificare.
            "notification_type": (
                notification_type_repository.get_instance_by_name("Reminder")
            ),
            # Titlul notificării.
            "title": "Event reminder",
            # Mesaj notificare.
            "message": ("Targ de Cariere USV 2026 " "starts tomorrow."),
            # Momentul programării notificării.
            "scheduled_at": aware(2026, 6, 9, 9),
            # Notificarea nu a fost încă trimisă.
            "sent_at": None,
            # Utilizatorul nu a citit notificarea.
            "is_read": False,
        },
        # =====================================================
        # REGISTRATION CONFIRMATION
        # =====================================================
        {
            # Utilizator destinatar.
            "user": student,
            # Eveniment asociat.
            "event": (
                event_repository.get_instance_by_name(
                    "Workshop Introducere " "in Inteligenta Artificiala"
                )
            ),
            # Tip notificare:
            # confirmare înscriere.
            "notification_type": (
                notification_type_repository.get_instance_by_name(
                    "Registration Confirmation"
                )
            ),
            # Titlu notificare.
            "title": "Registration confirmed",
            # Mesaj notificare.
            "message": ("Your registration was confirmed."),
            # Notificarea este trimisă imediat,
            # fără programare.
            "scheduled_at": None,
            # Data trimiterii notificării.
            "sent_at": timezone.now(),
            # Notificarea este deja citită.
            "is_read": True,
        },
    ]
