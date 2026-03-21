import os
import requests

from rest_framework_simplejwt.tokens import RefreshToken

from ..repository import UserRepository
from . import StareService, RolService, UserProfilesService

from .email_token import EmailTokenService
from .email import EmailService

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")


class GoogleAuthService:
    def __init__(self):
        self.stare_service = StareService()
        self.rol_service = RolService()
        self.profile_service = UserProfilesService()

        self.email_token_service = EmailTokenService()
        self.email_service = EmailService()

    def authenticate(self, access_token: str):
        try:
            response = requests.get(
                "https://www.googleapis.com/oauth2/v2/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
            )
            if response.status_code != 200:
                return None

            userinfo = response.json()
            email = userinfo["email"]

            user, created = UserRepository.get_or_create_google_user(email=email)

            if created:
                user.set_unusable_password()
                user.save()

                stare = self.stare_service.get_by_name("Activ")
                rol = self.rol_service.assign_role_from_email(email)

                self.profile_service.create(
                    user=user,
                    stare=stare,
                    rol=rol,
                )

                token_obj = self.email_token_service.create_token_for_user(user)

                self.email_service.send_complete_profile_email(user, token_obj.token)

            refresh = RefreshToken.for_user(user)

            return {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }

        except Exception:
            return None
