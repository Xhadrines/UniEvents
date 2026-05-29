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
    user_repository = UserRepository()
    organizer_repository = OrganizerRepository()
    location_repository = LocationRepository()
    category_repository = CategoryRepository()
    participation_type_repository = ParticipationTypeRepository()
    status_repository = StatusRepository()

    accepted_status = status_repository.get_instance_by_name("Acceptat")
    pending_status = status_repository.get_instance_by_name("In asteptare")
    finished_status = status_repository.get_instance_by_name("Finalizat")
    admin_user = user_repository.get_instance_by_username("administrator")

    return [
        {
            "name": "Workshop Introducere in Inteligenta Artificiala",
            "description": "Workshop practic pentru studenti interesati de AI, machine learning si Python.",
            "registration_link": "https://example.com/register/ai-workshop",
            "online_link": None,
            "organizer": organizer_repository.get_instance_by_name("FIRESC"),
            "location": location_repository.get_instance_by_name(
                "Laborator Inteligenta Artificiala"
            ),
            "category": category_repository.get_instance_by_name("Tehnologie si IT"),
            "participation_type": participation_type_repository.get_instance_by_name(
                "Fizic"
            ),
            "status": finished_status,
            "start_date": aware(2026, 4, 15, 10),
            "end_date": aware(2026, 4, 15, 14),
            "capacity": 25,
            "registration_deadline": aware(2026, 4, 14, 23, 59),
            "pricing_type": "free",
            "access_policy": "registration_ticket",
            "is_free_entry": True,
            "requires_registration": True,
            "requires_ticket": True,
            "max_files": 5,
            "max_file_size_mb": 20,
            "validated_by": admin_user,
            "validated_at": aware(2026, 4, 1, 12),
        },
        {
            "name": "Targ de Cariere USV 2026",
            "description": "Eveniment dedicat studentilor care doresc stagii, joburi si discutii cu angajatori.",
            "registration_link": "https://example.com/register/career-fair",
            "online_link": None,
            "organizer": organizer_repository.get_instance_by_name(
                "USV Computer Science Department"
            ),
            "location": location_repository.get_instance_by_name("Aula Magna"),
            "category": category_repository.get_instance_by_name(
                "Cariera si dezvoltare profesionala"
            ),
            "participation_type": participation_type_repository.get_instance_by_name(
                "Fizic"
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
        {
            "name": "Seminar Online Cybersecurity",
            "description": "Seminar online despre bune practici de securitate cibernetica.",
            "registration_link": "https://example.com/register/cybersecurity",
            "online_link": "https://meet.google.com/demo-cybersecurity",
            "organizer": organizer_repository.get_instance_by_name("FIRESC"),
            "location": location_repository.get_instance_by_name(
                "Online - Google Meet"
            ),
            "category": category_repository.get_instance_by_name("Tehnologie si IT"),
            "participation_type": participation_type_repository.get_instance_by_name(
                "Online"
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
