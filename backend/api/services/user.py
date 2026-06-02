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
    """
    Service responsabil pentru gestionarea utilizatorilor.

    Acest service gestionează:
    - înregistrarea utilizatorilor,
    - autentificarea,
    - resetarea parolei,
    - crearea profilului,
    - trimiterea email-urilor asociate contului.
    """

    def __init__(self):
        """
        Inițializăm toate repository-urile și service-urile necesare.

        Folosim:
        - UserRepository pentru utilizatori,
        - UserProfileService pentru profil,
        - RoleService pentru roluri,
        - StatusService pentru statusuri,
        - EmailService pentru email-uri,
        - EmailTokenService pentru token-uri.
        """

        super().__init__(UserRepository())

        # Salvăm repository-ul principal pentru acces rapid.
        self.user_repository = self.repository

        self.profile_service = UserProfileService()
        self.status_service = StatusService()
        self.role_service = RoleService()
        self.email_token_service = EmailTokenService()
        self.email_service = EmailService()

    def register(self, username: str, email: str, password: str):
        """
        Înregistrează un utilizator nou.

        Flow:
        1. Verificăm dacă utilizatorul există deja.
        2. Creăm utilizatorul.
        3. Stabilim statusul și rolul.
        4. Creăm profilul.
        5. Trimitem email-ul corespunzător.
        """

        # Verificăm dacă username-ul există deja.
        existing_user = self.user_repository.get_by_username(username)

        if existing_user:
            raise ValueError("User already exists")

        # Creăm utilizatorul nou.
        #
        # Parola este hash-uită automat.
        user = self.user_repository.create_user(
            username=username,
            email=email,
            password=password,
        )

        # Obținem statusul implicit.
        status = self.status_service.get_by_name("Activ")

        # Stabilim rolul utilizatorului pe baza email-ului.
        role = self.role_service.assign_role_from_email(user.email)

        # Creăm profilul utilizatorului.
        self.profile_service.create(
            user=user,
            status=status,
            role=role,
        )

        # Dacă utilizatorul este student,
        # trimitem email pentru completarea profilului.
        if role and role.name.lower() == "student":

            # Creăm token-ul pentru completarea profilului.
            token_obj = self.email_token_service.create_token_for_user(user)

            # Trimitem email-ul.
            self.email_service.send_complete_profile_email(
                user,
                token_obj.token,
            )

        # Pentru celelalte roluri,
        # trimitem email de bun venit.
        else:
            self.email_service.send_welcome_community_email(
                user=user,
                role=role,
            )

        return user

    def login(self, username_or_email: str, password: str):
        """
        Autentifică utilizatorul folosind:
        - username
        - sau email.

        Dacă autentificarea reușește,
        returnăm datele utilizatorului și profilului.
        """

        # Căutăm utilizatorul după username sau email.
        user = self.user_repository.get_user_by_username_or_email(username_or_email)

        # Verificăm:
        # - dacă utilizatorul există
        # - și dacă parola este corectă.
        if not user or not user.check_password(password):
            raise ValueError("Invalid credentials")

        # Obținem profilul utilizatorului.
        profile = self.profile_service.get_by_user_id(user.id)

        # Returnăm datele necesare frontend-ului.
        return {
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "date_joined": user.date_joined,
            # Dacă profilul nu există -> None.
            # Altfel -> returnăm datele profilului.
            "profile": (
                None
                if not profile
                else {
                    "id": profile.id,
                    # Date despre status.
                    "status": (
                        {
                            "id": profile.status.id,
                            "name": profile.status.name,
                        }
                        if profile.status
                        else None
                    ),
                    # Date despre rol.
                    "role": (
                        {
                            "id": profile.role.id,
                            "name": profile.role.name,
                        }
                        if profile.role
                        else None
                    ),
                    # Date despre facultate.
                    "faculty": (
                        {
                            "id": profile.faculty.id,
                            "name": profile.faculty.name,
                        }
                        if profile.faculty
                        else None
                    ),
                    # Date despre specializare.
                    "specialization": (
                        {
                            "id": profile.specialization.id,
                            "name": profile.specialization.name,
                        }
                        if profile.specialization
                        else None
                    ),
                    "study_year": profile.study_year,
                    "group": profile.group,
                    "semi_group": profile.semi_group,
                    # ID-ul Google al utilizatorului.
                    "google_sub": profile.google_sub,
                    # Spune dacă utilizatorul
                    # a fost autentificat prin Google.
                    "is_google_student": profile.is_google_student,
                    "created_at": profile.created_at,
                    "updated_at": profile.updated_at,
                }
            ),
        }

    def request_password_reset(self, email: str):
        """
        Inițiază procesul de resetare a parolei.

        Flow:
        1. Verificăm email-ul.
        2. Generăm token-ul de resetare.
        3. Trimitem email-ul cu link-ul de resetare.
        """

        # Verificăm dacă email-ul există în request.
        if not email:
            raise ValueError("Email is required")

        # Căutăm utilizatorul după email.
        user = self.user_repository.get_by_email(email)

        # Din motive de securitate,
        # dacă utilizatorul nu există,
        # nu aruncăm eroare.
        if not user:
            return

        # Encodăm ID-ul utilizatorului într-un format sigur pentru URL.
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        # Generăm token-ul securizat pentru resetare.
        token = default_token_generator.make_token(user)

        # Trimitem email-ul de resetare.
        self.email_service.send_password_reset_email(user, uid, token)

    def confirm_password_reset(self, uid: str, token: str, password: str):
        """
        Confirmă resetarea parolei.

        Flow:
        1. Decodăm UID-ul utilizatorului.
        2. Verificăm token-ul.
        3. Setăm parola nouă.
        """

        # Verificăm dacă toate datele necesare există.
        if not uid or not token or not password:
            raise ValueError("UID, token and password are required")

        try:
            # Decodăm UID-ul primit din URL.
            user_id = force_str(urlsafe_base64_decode(uid))

            # Căutăm utilizatorul după ID.
            user = self.user_repository.get_by_id(user_id)

        except Exception:
            # Dacă UID-ul este invalid,
            # oprim procesul.
            raise ValueError("Invalid reset link")

        # Dacă utilizatorul nu există.
        if not user:
            raise ValueError("Invalid reset link")

        # Verificăm dacă token-ul este valid
        # și nu a expirat.
        if not default_token_generator.check_token(user, token):
            raise ValueError("Invalid or expired token")

        # Salvăm noua parolă securizat.
        self.user_repository.set_password(user, password)
