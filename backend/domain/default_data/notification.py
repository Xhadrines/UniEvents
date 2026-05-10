from django.utils import timezone

from .utils import aware
from api.repository import UserRepository, EventRepository, NotificationTypeRepository


def default_notification_data():
    user_repository = UserRepository()
    event_repository = EventRepository()
    notification_type_repository = NotificationTypeRepository()

    student = user_repository.get_instance_by_username("student")
    event = event_repository.get_instance_by_name("Targ de Cariere USV 2026")

    return [
        {
            "user": student,
            "event": event,
            "notification_type": notification_type_repository.get_instance_by_name(
                "Reminder"
            ),
            "title": "Event reminder",
            "message": "Targ de Cariere USV 2026 starts tomorrow.",
            "scheduled_at": aware(2026, 6, 9, 9),
            "sent_at": None,
            "is_read": False,
        },
        {
            "user": student,
            "event": event_repository.get_instance_by_name(
                "Workshop Introducere in Inteligenta Artificiala"
            ),
            "notification_type": notification_type_repository.get_instance_by_name(
                "Registration Confirmation"
            ),
            "title": "Registration confirmed",
            "message": "Your registration was confirmed.",
            "scheduled_at": None,
            "sent_at": timezone.now(),
            "is_read": True,
        },
    ]
