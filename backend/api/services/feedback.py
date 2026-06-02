from django.utils import timezone

from .base_service import BaseService
from ..repository import FeedbackRepository


class FeedbackService(BaseService):
    """
    Service responsabil pentru gestionarea feedback-urilor.

    Acest service permite:
    - obținerea feedback-urilor unui eveniment,
    - obținerea feedback-urilor unui utilizator,
    - adăugarea feedback-ului după terminarea evenimentului.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu FeedbackRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Feedback.
        """

        super().__init__(FeedbackRepository())

    def get_by_event(self, event_id: int):
        """
        Returnează toate feedback-urile
        asociate unui eveniment.
        """

        return self.repository.get_by_event(event_id)

    def get_by_user(self, user_id: int):
        """
        Returnează toate feedback-urile
        trimise de un utilizator.
        """

        return self.repository.get_by_user(user_id)

    def create_feedback(self, user, event, rating: int, comment: str = ""):
        """
        Creează feedback pentru un eveniment.

        Reguli importante:
        - feedback-ul poate fi adăugat doar după terminarea evenimentului,
        - un utilizator poate adăuga un singur feedback per eveniment.
        """

        # Verificăm dacă evenimentul s-a terminat.
        #
        # Dacă data curentă este mai mică decât data de final,
        # înseamnă că evenimentul încă este activ.
        if timezone.now() < event.end_date:
            raise ValueError("Feedback can be added only after the event has ended")

        # Verificăm dacă utilizatorul a mai trimis feedback.
        existing_feedback = self.repository.get_by_user_and_event(user.id, event.id)

        # Dacă există deja feedback,
        # oprim procesul pentru a evita duplicatele.
        if existing_feedback:
            raise ValueError("User already added feedback for this event")

        # Creăm feedback-ul nou.
        return self.repository.create(
            user=user,
            event=event,
            rating=rating,
            comment=comment,
        )
