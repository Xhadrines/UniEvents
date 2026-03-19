from .base_service import BaseService

from ..repository import UserRepository

from .user_profiles import UserProfilesService
from .stare import StareService
from .rol import RolService


class UserService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())
        self.user_repo = self.repository
        self.profile_service = UserProfilesService()
        self.stare_service = StareService()
        self.rol_service = RolService()

    def register(self, username: str, email: str, password: str):
        existing_user = self.user_repo.get_instance_by_username(username)

        if existing_user:
            raise ValueError("User already exists")

        user = self.user_repo.create_user(username, email, password)

        stare = self.stare_service.get_by_name("Activ")
        rol = self.rol_service.get_by_name("Student")

        self.profile_service.create(
            user=user,
            stare=stare,
            rol=rol,
        )

        return user

    def login(self, username_or_email: str, password: str):
        user = self.user_repo.get_user_by_username_or_email(username_or_email)

        if not user or not user.check_password(password):
            raise ValueError("Invalid credentials")

        profile = self.profile_service.get_by_user_id(user.id)

        if not profile:
            return {
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                "profile": None,
            }

        return {
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "profile": {
                "id": profile.id,
                "stare": profile.stare_id,
                "rol": profile.rol_id,
                "facultate": profile.facultate_id,
                "specializare": profile.specializare_id,
                "an_studiu": profile.an_studiu,
                "grupa": profile.grupa,
                "semi_grupa": profile.semi_grupa,
            },
        }
