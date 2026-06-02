from .base_service import BaseService

from ..repository import EmailTokenRepository


class EmailTokenService(BaseService):
    """
    Service responsabil pentru gestionarea token-urilor de email.

    Token-urile sunt folosite, de regulă, pentru:
    - confirmarea contului,
    - resetarea parolei,
    - validarea unor acțiuni sensibile.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu EmailTokenRepository.

        Astfel, toate metodele moștenite din BaseService
        vor lucra pe modelul EmailToken.
        """

        super().__init__(EmailTokenRepository())

    def create_token_for_user(self, user):
        """
        Creează un token nou pentru utilizator.

        Token-ul va fi asociat utilizatorului primit ca parametru.
        """

        return self.repository.create(user=user)

    def validate_token(self, token):
        """
        Verifică dacă token-ul este valid.

        Un token este considerat invalid dacă:
        - nu există în baza de date,
        - sau a fost deja folosit.
        """

        # Căutăm token-ul în baza de date.
        token_obj = self.repository.get_by_token(token)

        # Dacă token-ul nu există sau este deja folosit,
        # returnăm None.
        if not token_obj or token_obj.is_used:
            return None

        # Returnăm obiectul token valid.
        return token_obj

    def mark_as_used(self, token_obj):
        """
        Marchează token-ul ca fiind folosit.

        Astfel prevenim reutilizarea aceluiași token,
        ceea ce este important pentru securitate.
        """

        # Setăm token-ul ca folosit.
        token_obj.is_used = True

        # Salvăm modificarea în baza de date.
        token_obj.save()

        return token_obj
