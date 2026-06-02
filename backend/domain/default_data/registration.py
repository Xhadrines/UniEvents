from .utils import aware
from api.repository import (
    UserRepository,
    EventRepository,
    StatusRepository,
)


def default_registration_data():
    """
    Returnează datele default pentru înscrierile
    la evenimente.

    Aceste date sunt utilizate pentru:
    - seed-ul inițial al bazei de date,
    - testare,
    - dezvoltare.
    """

    # =====================================================
    # REPOSITORIES
    # =====================================================

    user_repository = UserRepository()

    event_repository = EventRepository()

    status_repository = StatusRepository()

    # =====================================================
    # STATUSURI
    # =====================================================

    accepted_status = status_repository.get_instance_by_name("Acceptat")

    waiting_status = status_repository.get_instance_by_name("Lista de asteptare")

    return [
        # =====================================================
        # STUDENT -> AI WORKSHOP
        # =====================================================
        {
            # Utilizatorul înscris.
            "user": (user_repository.get_instance_by_username("student")),
            # Evenimentul la care este înscris.
            "event": (
                event_repository.get_instance_by_name(
                    "Workshop Introducere " "in Inteligenta Artificiala"
                )
            ),
            # Status înscriere:
            # acceptat.
            "status": accepted_status,
            # Email-ul de confirmare a fost trimis.
            "confirmation_email_sent": True,
            # QR code-ul asociat biletului.
            "ticket_qr_code": ("tickets/qr_codes/" "student_ai_workshop.png"),
            # Participantul a făcut check-in.
            "checked_in": True,
            # Ora check-in-ului.
            "checked_in_at": aware(2026, 4, 15, 9, 55),
        },
        # =====================================================
        # GUEST -> CAREER FAIR
        # =====================================================
        {
            # Utilizatorul înscris.
            "user": (user_repository.get_instance_by_username("guest")),
            # Evenimentul asociat.
            "event": (
                event_repository.get_instance_by_name("Targ de Cariere USV 2026")
            ),
            # Utilizator aflat în lista de așteptare.
            "status": waiting_status,
            # Email-ul de confirmare
            # nu a fost trimis.
            "confirmation_email_sent": False,
            # Participantul nu a făcut check-in.
            "checked_in": False,
        },
    ]
