from .base_repository import BaseRepository

from ..models import EmailToken


class EmailTokenRepository(BaseRepository):
    def __init__(self):
        super().__init__(EmailToken)

    def get_by_token(self, token):
        # Returneaza token-ul de email
        return self.model.objects.filter(token=token).first()
