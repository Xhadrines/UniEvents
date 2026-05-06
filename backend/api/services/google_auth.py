import requests

from rest_framework_simplejwt.tokens import RefreshToken

from ..repository import UserRepository

from .status import StatusService
from .role import RoleService
from .user_profile import UserProfileService
from .email_token import EmailTokenService
from .email import EmailService


class GoogleAuthService:
    # Service pentru autentificarea studentilor cu Google OAuth

    def __init__(self):
        self.user_repository = UserRepository()
        self.status_service = StatusService()
        self.role_service = RoleService()
        self.profile_service = UserProfileService()
        self.email_token_service = EmailTokenService()
        self.email_service = EmailService()

    def authenticate(self, access_token: str):
        try:
            response = requests.get(
                "https://www.googleapis.com/oauth2/v2/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
                timeout=10,
            )

            if response.status_code != 200:
                return None

            userinfo = response.json()
            email = userinfo.get("email")
            google_sub = userinfo.get("id")

            if not email or not email.endswith("@student.usv.ro"):
                return None

            user, created = self.user_repository.get_or_create_google_user(email=email)

            if created:
                user.set_unusable_password()
                user.save()

                status = self.status_service.get_by_name("Activ")
                role = self.role_service.assign_role_from_email(email)

                self.profile_service.create(
                    user=user,
                    status=status,
                    role=role,
                    google_sub=google_sub,
                    is_google_student=True,
                )

                token_obj = self.email_token_service.create_token_for_user(user)
                self.email_service.send_complete_profile_email(user, token_obj.token)

            profile = self.profile_service.get_by_user_id(user.id)
            refresh = RefreshToken.for_user(user)

            return {
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "profile": (
                    None
                    if not profile
                    else {
                        "id": profile.id,
                        "status": profile.status_id,
                        "role": profile.role_id,
                        "faculty": profile.faculty_id,
                        "specialization": profile.specialization_id,
                        "study_year": profile.study_year,
                        "group": profile.group,
                        "semi_group": profile.semi_group,
                    }
                ),
                "created": created,
            }

        except requests.RequestException:
            return None
