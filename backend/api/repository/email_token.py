from .base_repository import BaseRepository

from domain.models import EmailToken


class EmailTokenRepository(BaseRepository):
    """
    Repository responsabil pentru operațiile legate de EmailToken.

    Acest model este folosit, de regulă, pentru:
    - confirmarea email-ului,
    - resetarea parolei,
    - validarea unor acțiuni prin token.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul EmailToken.

        Toate metodele moștenite din BaseRepository
        vor lucra automat pe tabela EmailToken.
        """

        super().__init__(EmailToken)

    def get_by_token(self, token):
        """
        Caută un token în baza de date.

        Folosim această metodă pentru a verifica dacă:
        - token-ul există,
        - token-ul este valid,
        - token-ul poate fi folosit pentru activare/resetare/etc.
        """

        # Returnăm primul token găsit.
        # Dacă nu există, se returnează None.
        return self.model.objects.filter(token=token).first()
