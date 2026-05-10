from api.repository import SponsorRepository, EventRepository


def default_event_sponsor_data():
    sponsor_repository = SponsorRepository()
    event_repository = EventRepository()

    ai_event = event_repository.get_instance_by_name(
        "Workshop Introducere in Inteligenta Artificiala"
    )
    career_event = event_repository.get_instance_by_name("Targ de Cariere USV 2026")

    return [
        {
            "sponsor": sponsor_repository.get_instance_by_name("ASSIST Software"),
            "event": ai_event,
        },
        {
            "sponsor": sponsor_repository.get_instance_by_name("Bitdefender"),
            "event": ai_event,
        },
        {
            "sponsor": sponsor_repository.get_instance_by_name("EGGER Romania"),
            "event": career_event,
        },
    ]
