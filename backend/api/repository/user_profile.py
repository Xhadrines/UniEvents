from .base_repository import BaseRepository

from domain.models import UserProfile


class UserProfileRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea profilurilor utilizatorilor.

    Profilul utilizatorului poate conține informații suplimentare precum:
    - facultatea,
    - specializarea,
    - poza de profil,
    - date personale,
    - preferințe.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul UserProfile.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela UserProfile.
        """

        super().__init__(UserProfile)

    def get_by_user(self, user_id: int):
        """
        Returnează profilul asociat unui utilizator.

        Deoarece un utilizator are, de regulă,
        un singur profil, folosim first().
        """

        # Căutăm primul profil asociat utilizatorului.
        return self.model.objects.filter(user_id=user_id).first()

    def get_by_user_id(self, user_id: int):
        """
        Alias pentru get_by_user().

        Metoda a fost păstrată pentru:
        - compatibilitate,
        - lizibilitate,
        - cod mai vechi din aplicație.
        """

        return self.get_by_user(user_id)
