from django.contrib.auth.models import User
from django.db.models import Q

from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def get_by_username(self, username: str):
        # Returneaza utilizatorul dupa username
        return self.model.objects.filter(username=username).first()

    def get_instance_by_username(self, username: str):
        # Alias pentru compatibilitate cu datele default
        return self.get_by_username(username)

    def get_by_email(self, email: str):
        # Returneaza utilizatorul dupa email
        return self.model.objects.filter(email=email).first()

    def get_user_by_username_or_email(self, username_or_email: str):
        # Cauta utilizator dupa username sau email
        return self.model.objects.filter(
            Q(username=username_or_email) | Q(email=username_or_email)
        ).first()

    def create_user(self, **data):
        # Creeaza utilizator cu parola criptata
        password = data.pop("password", None)
        user = self.model(**data)

        if password:
            user.set_password(password)

        user.save()
        return user

    def get_or_create_google_user(self, email: str):
        # Creeaza sau returneaza userul autentificat prin Google
        username = email.split("@")[0]

        return self.model.objects.get_or_create(
            email=email,
            defaults={
                "username": username,
                "is_active": True,
            },
        )

    def username_exists_for_other_user(self, username: str, user_id: int) -> bool:
        return self.model.objects.filter(username=username).exclude(id=user_id).exists()

    def update_profile_fields(
        self, user, username=None, first_name=None, last_name=None
    ):
        if username is not None:
            user.username = username

        if first_name is not None:
            user.first_name = first_name

        if last_name is not None:
            user.last_name = last_name

        user.save()
        return user
