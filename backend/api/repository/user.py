from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model

from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def get_instance_by_username(self, username):
        return self.model.objects.filter(username=username).first()

    def get_id_by_username(self, username):
        obj = self.model.objects.filter(username=username).only("id").first()
        return obj.id if obj else None

    def get_all_by_username(self, username):
        return self.model.objects.filter(username=username)

    def create_user(self, username, email, password):
        return self.model.objects.create_user(
            username=username, email=email, password=password
        )

    def authenticate_user(self, username, password):
        return authenticate(username=username, password=password)

    def get_user_by_username_or_email(self, username_or_email: str):
        User = get_user_model()

        try:
            return User.objects.get(
                models.Q(username=username_or_email) | models.Q(email=username_or_email)
            )
        except User.DoesNotExist:
            return None
