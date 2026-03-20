from ..repository import EmailTokenRepository


class EmailTokenService:
    def __init__(self):
        self.repo = EmailTokenRepository()

    def create_token_for_user(self, user):
        return self.repo.create(user=user)

    def validate_token(self, token):
        return self.repo.get_by_token(token)

    def mark_as_used(self, token_obj):
        token_obj.is_used = True
        token_obj.save()
