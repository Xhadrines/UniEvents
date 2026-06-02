from .base_repository import BaseRepository

from domain.models import Registration


class RegistrationRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea înscrierilor la evenimente.

    Acest repository permite:
    - obținerea înscrierilor unui utilizator,
    - obținerea participanților unui eveniment,
    - verificarea dacă un utilizator este înscris la un eveniment.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Registration.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela Registration.
        """

        super().__init__(Registration)

    def get_by_user(self, user_id: int):
        """
        Returnează toate înscrierile unui utilizator.

        Practic obținem toate evenimentele
        la care utilizatorul s-a înscris.
        """

        return self.model.objects.filter(user_id=user_id)

    def get_by_event(self, event_id: int):
        """
        Returnează toate înscrierile pentru un eveniment.

        Practic obținem lista participanților
        înscriși la acel eveniment.
        """

        return self.model.objects.filter(event_id=event_id)

    def get_by_user_and_event(self, user_id: int, event_id: int):
        """
        Verifică dacă un utilizator este înscris
        la un anumit eveniment.

        Folosim această metodă pentru:
        - validări,
        - evitarea înscrierilor duplicate,
        - verificarea accesului la anumite funcționalități.
        """

        # Returnăm primul rezultat găsit.
        # Dacă utilizatorul nu este înscris,
        # se returnează None.
        return self.model.objects.filter(user_id=user_id, event_id=event_id).first()
