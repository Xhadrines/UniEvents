from api.repository import SponsorRepository, EventRepository


def default_event_sponsor_data():
    """
    Returnează datele default pentru relațiile
    dintre sponsori și evenimente.

    Aceste date sunt folosite pentru:
    - popularea inițială a bazei de date,
    - dezvoltare,
    - testare.
    """

    # Inițializăm repository-urile necesare.
    sponsor_repository = SponsorRepository()

    event_repository = EventRepository()

    # =====================================================
    # EVENIMENTE
    # =====================================================

    # Eveniment AI.
    ai_event = event_repository.get_instance_by_name(
        "Workshop Introducere in Inteligenta Artificiala"
    )

    # Eveniment carieră.
    career_event = event_repository.get_instance_by_name("Targ de Cariere USV 2026")

    return [
        # =====================================================
        # ASSIST SOFTWARE -> AI EVENT
        # =====================================================
        {
            # Sponsorul evenimentului.
            "sponsor": sponsor_repository.get_instance_by_name("ASSIST Software"),
            # Evenimentul sponsorizat.
            "event": ai_event,
        },
        # =====================================================
        # BITDEFENDER -> AI EVENT
        # =====================================================
        {
            # Sponsorul evenimentului.
            "sponsor": sponsor_repository.get_instance_by_name("Bitdefender"),
            # Evenimentul sponsorizat.
            "event": ai_event,
        },
        # =====================================================
        # EGGER -> CAREER EVENT
        # =====================================================
        {
            # Sponsorul evenimentului.
            "sponsor": sponsor_repository.get_instance_by_name("EGGER Romania"),
            # Evenimentul sponsorizat.
            "event": career_event,
        },
    ]
