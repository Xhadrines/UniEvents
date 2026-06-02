from .utils import aware

from api.repository import (
    UserRepository,
    OrganizerRepository,
    LocationRepository,
    CategoryRepository,
    ParticipationTypeRepository,
    StatusRepository,
)


def default_event_data():
    """
    Returnează lista de evenimente default
    folosită pentru popularea inițială a bazei de date.

    Evenimentele includ:
    - workshop-uri,
    - târguri de carieră,
    - seminarii online.
    """

    # =====================================================
    # REPOSITORIES
    # =====================================================

    user_repository = UserRepository()

    organizer_repository = OrganizerRepository()

    location_repository = LocationRepository()

    category_repository = CategoryRepository()

    participation_type_repository = ParticipationTypeRepository()

    status_repository = StatusRepository()

    # =====================================================
    # STATUSURI
    # =====================================================

    accepted_status = status_repository.get_instance_by_name("Acceptat")

    pending_status = status_repository.get_instance_by_name("In asteptare")

    finished_status = status_repository.get_instance_by_name("Finalizat")

    # =====================================================
    # ADMIN
    # =====================================================

    # Administratorul care validează evenimentele.
    admin_user = user_repository.get_instance_by_username("administrator")

    return [
        # =====================================================
        # AI WORKSHOP
        # =====================================================
        {
            # Titlul evenimentului.
            "name": ("Workshop Introducere " "in Inteligenta Artificiala"),
            # Descrierea evenimentului.
            "description": (
                "Workshop practic pentru studenti "
                "interesati de AI, machine learning si Python."
            ),
            # Link pentru înscriere.
            "registration_link": ("https://example.com/register/ai-workshop"),
            # Eveniment fizic -> fără link online.
            "online_link": None,
            # Organizatorul evenimentului.
            "organizer": (organizer_repository.get_instance_by_name("FIRESC")),
            # Locația evenimentului.
            "location": (
                location_repository.get_instance_by_name(
                    "Laborator Inteligenta Artificiala"
                )
            ),
            # Categoria evenimentului.
            "category": (category_repository.get_instance_by_name("Tehnologie si IT")),
            # Tip participare.
            "participation_type": (
                participation_type_repository.get_instance_by_name("Fizic")
            ),
            # Status eveniment.
            "status": finished_status,
            # Data de început.
            "start_date": aware(2026, 4, 15, 10),
            # Data de final.
            "end_date": aware(2026, 4, 15, 14),
            # Număr maxim participanți.
            "capacity": 25,
            # Deadline înscriere.
            "registration_deadline": aware(2026, 4, 14, 23, 59),
            # Eveniment gratuit.
            "pricing_type": "free",
            # Politica accesului.
            "access_policy": "registration_ticket",
            # Intrare gratuită.
            "is_free_entry": True,
            # Necesită înscriere.
            "requires_registration": True,
            # Necesită bilet.
            "requires_ticket": True,
            # Număr maxim fișiere.
            "max_files": 5,
            # Dimensiune maximă fișiere.
            "max_file_size_mb": 20,
            # Administrator validare.
            "validated_by": admin_user,
            # Data validării.
            "validated_at": aware(2026, 4, 1, 12),
        },
        # =====================================================
        # CAREER FAIR
        # =====================================================
        {
            "name": "Targ de Cariere USV 2026",
            "description": (
                "Eveniment dedicat studentilor "
                "care doresc stagii, joburi si "
                "discutii cu angajatori."
            ),
            "registration_link": ("https://example.com/register/career-fair"),
            "online_link": None,
            "organizer": (
                organizer_repository.get_instance_by_name(
                    "USV Computer Science Department"
                )
            ),
            "location": (location_repository.get_instance_by_name("Aula Magna")),
            "category": (
                category_repository.get_instance_by_name(
                    "Cariera si dezvoltare profesionala"
                )
            ),
            "participation_type": (
                participation_type_repository.get_instance_by_name("Fizic")
            ),
            "status": accepted_status,
            "start_date": aware(2026, 6, 10, 9),
            "end_date": aware(2026, 6, 10, 16),
            "capacity": 300,
            "registration_deadline": aware(2026, 6, 9, 23, 59),
            "pricing_type": "free",
            "access_policy": "open",
            "is_free_entry": True,
            "requires_registration": False,
            "requires_ticket": False,
            "max_files": 10,
            "max_file_size_mb": 50,
            "validated_by": admin_user,
            "validated_at": aware(2026, 5, 1, 10),
        },
        # =====================================================
        # CYBERSECURITY WEBINAR
        # =====================================================
        {
            "name": "Seminar Online Cybersecurity",
            "description": (
                "Seminar online despre bune practici " "de securitate cibernetica."
            ),
            "registration_link": ("https://example.com/register/cybersecurity"),
            # Link Google Meet.
            "online_link": ("https://meet.google.com/demo-cybersecurity"),
            "organizer": (organizer_repository.get_instance_by_name("FIRESC")),
            "location": (
                location_repository.get_instance_by_name("Online - Google Meet")
            ),
            "category": (category_repository.get_instance_by_name("Tehnologie si IT")),
            "participation_type": (
                participation_type_repository.get_instance_by_name("Online")
            ),
            "status": pending_status,
            "start_date": aware(2026, 7, 5, 18),
            "end_date": aware(2026, 7, 5, 20),
            "capacity": 100,
            "registration_deadline": aware(2026, 7, 4, 23, 59),
            "pricing_type": "free",
            "access_policy": "registration",
            "is_free_entry": True,
            "requires_registration": True,
            "requires_ticket": False,
            "max_files": 3,
            "max_file_size_mb": 10,
        },
    ]
