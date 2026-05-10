from .utils import aware
from api.repository import UserRepository, EventRepository, StatusRepository


def default_registration_data():
    user_repository = UserRepository()
    event_repository = EventRepository()
    status_repository = StatusRepository()

    accepted_status = status_repository.get_instance_by_name("Acceptat")
    waiting_status = status_repository.get_instance_by_name("Lista de asteptare")

    return [
        {
            "user": user_repository.get_instance_by_username("student"),
            "event": event_repository.get_instance_by_name(
                "Workshop Introducere in Inteligenta Artificiala"
            ),
            "status": accepted_status,
            "confirmation_email_sent": True,
            "ticket_qr_code": "tickets/qr_codes/student_ai_workshop.png",
            "checked_in": True,
            "checked_in_at": aware(2026, 4, 15, 9, 55),
        },
        {
            "user": user_repository.get_instance_by_username("guest"),
            "event": event_repository.get_instance_by_name("Targ de Cariere USV 2026"),
            "status": waiting_status,
            "confirmation_email_sent": False,
            "checked_in": False,
        },
    ]
