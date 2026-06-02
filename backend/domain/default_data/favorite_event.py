from api.repository import UserRepository, EventRepository


def default_favorite_event_data():
    """
    Returnează datele default pentru evenimentele favorite.

    Aceste date sunt utilizate pentru:
    - seed-ul bazei de date,
    - dezvoltare,
    - testare.
    """

    # Inițializăm repository-urile necesare.
    user_repository = UserRepository()

    event_repository = EventRepository()

    return [
        # =====================================================
        # STUDENT -> TARG DE CARIERE
        # =====================================================
        {
            # Utilizatorul care a adăugat evenimentul la favorite.
            "user": (user_repository.get_instance_by_username("student")),
            # Evenimentul favorit.
            "event": (
                event_repository.get_instance_by_name("Targ de Cariere USV 2026")
            ),
        },
        # =====================================================
        # GUEST -> CYBERSECURITY
        # =====================================================
        {
            # Utilizatorul care a adăugat evenimentul la favorite.
            "user": (user_repository.get_instance_by_username("guest")),
            # Evenimentul favorit.
            "event": (
                event_repository.get_instance_by_name("Seminar Online Cybersecurity")
            ),
        },
    ]
