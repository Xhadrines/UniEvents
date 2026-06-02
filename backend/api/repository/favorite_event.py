from .base_repository import BaseRepository

from domain.models import FavoriteEvent


class FavoriteEventRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea evenimentelor favorite.

    Acest model face legătura dintre:
    - utilizatori
    - evenimentele salvate ca favorite.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul FavoriteEvent.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela FavoriteEvent.
        """

        super().__init__(FavoriteEvent)

    def get_by_user(self, user_id: int):
        """
        Returnează toate evenimentele favorite
        ale unui utilizator.
        """

        # Filtrăm toate înregistrările care aparțin utilizatorului.
        return self.model.objects.filter(user_id=user_id)

    def get_by_user_and_event(self, user_id: int, event_id: int):
        """
        Verifică dacă un anumit eveniment este favorit
        pentru un utilizator.

        Folosim această metodă, de exemplu:
        - pentru a verifica dacă utilizatorul a salvat deja evenimentul,
        - pentru a evita duplicatele.
        """

        # Returnăm primul rezultat găsit.
        # Dacă nu există, se returnează None.
        return self.model.objects.filter(user_id=user_id, event_id=event_id).first()
