from api.repository import UserRepository, EventRepository


def default_feedback_data():
    user_repository = UserRepository()
    event_repository = EventRepository()

    return [
        {
            "user": user_repository.get_instance_by_username("student"),
            "event": event_repository.get_instance_by_name(
                "Workshop Introducere in Inteligenta Artificiala"
            ),
            "rating": 5,
            "comment": "Workshop foarte util, cu exemple clare si aplicatii practice.",
            "sentiment_score": 0.92,
            "sentiment_label": "positive",
        },
        {
            "user": user_repository.get_instance_by_username("guest"),
            "event": event_repository.get_instance_by_name(
                "Workshop Introducere in Inteligenta Artificiala"
            ),
            "rating": 4,
            "comment": "Eveniment bun, dar ar fi fost util mai mult timp pentru exercitii.",
            "sentiment_score": 0.65,
            "sentiment_label": "positive",
        },
    ]
