from .base_service import BaseService

from ..repository import EmailTokenRepository


class EmailTokenService(BaseService):
    def __init__(self):
        super().__init__(EmailTokenRepository())

    def create_token_for_user(self, user):
        return self.repository.create(user=user)

    def validate_token(self, token):
        token_obj = self.repository.get_by_token(token)

        if not token_obj or token_obj.is_used:
            return None

        return token_obj

    def mark_as_used(self, token_obj):
        token_obj.is_used = True
        token_obj.save()
        return token_obj
