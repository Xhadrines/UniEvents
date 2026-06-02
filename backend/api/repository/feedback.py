from .base_repository import BaseRepository

from domain.models import Feedback


class FeedbackRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea feedback-urilor.

    Acest repository permite:
    - obținerea feedback-urilor unui eveniment,
    - obținerea feedback-urilor unui utilizator,
    - verificarea feedback-ului unui utilizator pentru un eveniment.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Feedback.

        Toate metodele moștenite din BaseRepository
        vor lucra pe tabela Feedback.
        """

        super().__init__(Feedback)

    def get_by_event(self, event_id: int):
        """
        Returnează toate feedback-urile asociate unui eveniment.
        """

        # Filtrăm toate feedback-urile după ID-ul evenimentului.
        return self.model.objects.filter(event_id=event_id)

    def get_by_user(self, user_id: int):
        """
        Returnează toate feedback-urile trimise de un utilizator.
        """

        # Filtrăm toate feedback-urile după utilizator.
        return self.model.objects.filter(user_id=user_id)

    def get_by_user_and_event(self, user_id: int, event_id: int):
        """
        Returnează feedback-ul unui utilizator pentru un anumit eveniment.

        Folosim această metodă pentru:
        - a verifica dacă utilizatorul a oferit deja feedback,
        - a evita feedback-urile duplicate.
        """

        # Returnăm primul rezultat găsit.
        # Dacă nu există feedback, se returnează None.
        return self.model.objects.filter(user_id=user_id, event_id=event_id).first()
