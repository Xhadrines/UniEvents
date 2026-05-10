from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from .base_service import BaseService
from ..repository import UserRepository

from .user_profile import UserProfileService
from .status import StatusService
from .role import RoleService
from .email_token import EmailTokenService
from .email import EmailService


class UserService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())

        self.user_repository = self.repository
        self.profile_service = UserProfileService()
        self.status_service = StatusService()
        self.role_service = RoleService()
        self.email_token_service = EmailTokenService()
        self.email_service = EmailService()

    def register(self, username: str, email: str, password: str):
        # Inregistreaza un utilizator nou si creeaza profilul lui
        existing_user = self.user_repository.get_by_username(username)

        if existing_user:
            raise ValueError("User already exists")

        user = self.user_repository.create_user(
            username=username,
            email=email,
            password=password,
        )

        status = self.status_service.get_by_name("Activ")
        role = self.role_service.assign_role_from_email(user.email)

        self.profile_service.create(
            user=user,
            status=status,
            role=role,
        )

        token_obj = self.email_token_service.create_token_for_user(user)
        self.email_service.send_complete_profile_email(user, token_obj.token)

        return user

    def login(self, username_or_email: str, password: str):
        # Autentifica utilizatorul cu username sau email
        user = self.user_repository.get_user_by_username_or_email(username_or_email)

        if not user or not user.check_password(password):
            raise ValueError("Invalid credentials")

        profile = self.profile_service.get_by_user_id(user.id)

        return {
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
        }

    def request_password_reset(self, email: str):
        if not email:
            raise ValueError("Email is required")

        user = self.user_repository.get_by_email(email)

        if not user:
            return

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        self.email_service.send_password_reset_email(user, uid, token)

    def confirm_password_reset(self, uid: str, token: str, password: str):
        if not uid or not token or not password:
            raise ValueError("UID, token and password are required")

        try:
            user_id = force_str(urlsafe_base64_decode(uid))
            user = self.user_repository.get_by_id(user_id)
        except Exception:
            raise ValueError("Invalid reset link")

        if not user:
            raise ValueError("Invalid reset link")

        if not default_token_generator.check_token(user, token):
            raise ValueError("Invalid or expired token")

        self.user_repository.set_password(user, password)
