from api.repository import UserRepository, EventRepository


def default_feedback_data():
    """
    Returnează datele default pentru feedback-urile
    asociate evenimentelor.

    Aceste date sunt folosite pentru:
    - seed-ul inițial al bazei de date,
    - testare,
    - dezvoltare.
    """

    # Inițializăm repository-urile necesare.
    user_repository = UserRepository()

    event_repository = EventRepository()

    return [
        # =====================================================
        # FEEDBACK STUDENT
        # =====================================================
        {
            # Utilizatorul care a oferit feedback-ul.
            "user": (user_repository.get_instance_by_username("student")),
            # Evenimentul evaluat.
            "event": (
                event_repository.get_instance_by_name(
                    "Workshop Introducere " "in Inteligenta Artificiala"
                )
            ),
            # Rating-ul acordat evenimentului.
            #
            # Scală:
            # 1 - foarte slab
            # 5 - excelent
            "rating": 5,
            # Comentariul utilizatorului.
            "comment": (
                "Workshop foarte util, " "cu exemple clare si aplicatii practice."
            ),
            # Scorul de sentiment generat automat.
            #
            # Valori apropiate de 1
            # indică sentiment pozitiv.
            "sentiment_score": 0.92,
            # Eticheta sentimentului.
            "sentiment_label": "positive",
        },
        # =====================================================
        # FEEDBACK GUEST
        # =====================================================
        {
            # Utilizatorul care a oferit feedback-ul.
            "user": (user_repository.get_instance_by_username("guest")),
            # Evenimentul evaluat.
            "event": (
                event_repository.get_instance_by_name(
                    "Workshop Introducere " "in Inteligenta Artificiala"
                )
            ),
            # Rating-ul acordat.
            "rating": 4,
            # Comentariu feedback.
            "comment": (
                "Eveniment bun, dar ar fi fost util " "mai mult timp pentru exercitii."
            ),
            # Scorul de sentiment.
            "sentiment_score": 0.65,
            # Eticheta sentimentului.
            "sentiment_label": "positive",
        },
    ]
