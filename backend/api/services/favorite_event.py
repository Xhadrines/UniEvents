from .base_service import BaseService

from ..repository import FavoriteEventRepository


class FavoriteEventService(BaseService):
    """
    Service responsabil pentru gestionarea evenimentelor favorite.

    Acest service permite:
    - obținerea favoritelor unui utilizator,
    - adăugarea unui eveniment la favorite,
    - eliminarea unui eveniment din favorite.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu FavoriteEventRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul FavoriteEvent.
        """

        super().__init__(FavoriteEventRepository())

    def get_by_user(self, user_id: int):
        """
        Returnează toate evenimentele favorite
        ale unui utilizator.
        """

        return self.repository.get_by_user(user_id)

    def add_to_favorites(self, user, event):
        """
        Adaugă un eveniment la favorite.

        Înainte de creare verificăm dacă evenimentul
        există deja în lista de favorite,
        pentru a evita duplicatele.
        """

        # Verificăm dacă relația utilizator-eveniment există deja.
        favorite = self.repository.get_by_user_and_event(user.id, event.id)

        # Dacă există deja la favorite,
        # returnăm obiectul existent.
        if favorite:
            return favorite

        # Dacă nu există, creăm înregistrarea nouă.
        return self.repository.create(user=user, event=event)

    def remove_from_favorites(self, user_id: int, event_id: int):
        """
        Elimină un eveniment din lista de favorite.
        """

        # Căutăm relația dintre utilizator și eveniment.
        favorite = self.repository.get_by_user_and_event(user_id, event_id)

        # Dacă relația nu există,
        # nu avem ce șterge.
        if not favorite:
            return False

        # Ștergem evenimentul din favorite.
        favorite.delete()

        return True
