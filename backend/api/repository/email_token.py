from .base_repository import BaseRepository

from ..models.email_token import EmailToken


class EmailTokenRepository(BaseRepository):
    def __init__(self):
        super().__init__(EmailToken)

    def get_by_token(self, token):
        return self.model.objects.filter(token=token, is_used=False).first()
