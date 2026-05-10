from api.repository import UserRepository, EventRepository


def default_favorite_event_data():
    user_repository = UserRepository()
    event_repository = EventRepository()

    return [
        {
            "user": user_repository.get_instance_by_username("student"),
            "event": event_repository.get_instance_by_name("Targ de Cariere USV 2026"),
        },
        {
            "user": user_repository.get_instance_by_username("guest"),
            "event": event_repository.get_instance_by_name(
                "Seminar Online Cybersecurity"
            ),
        },
    ]
