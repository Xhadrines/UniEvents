import requests

from rest_framework_simplejwt.tokens import RefreshToken

from ..repository import UserRepository

from .status import StatusService
from .role import RoleService
from .user_profile import UserProfileService
from .email_token import EmailTokenService
from .email import EmailService


class GoogleAuthService:
    """
    Service responsabil pentru autentificarea studenților prin Google OAuth.

    Acest service verifică token-ul primit de la Google,
    obține datele utilizatorului și creează contul în aplicație
    dacă studentul nu există deja.

    Important:
    Sunt acceptați doar utilizatorii cu email instituțional
    care se termină în @student.usv.ro.
    """

    def __init__(self):
        """
        Inițializăm toate repository-urile și service-urile
        necesare pentru autentificarea cu Google.

        Pe scurt:
        - UserRepository gestionează utilizatorul Django,
        - StatusService oferă statusul contului,
        - RoleService stabilește rolul utilizatorului,
        - UserProfileService creează profilul utilizatorului,
        - EmailTokenService creează token-ul pentru completarea profilului,
        - EmailService trimite email-ul către utilizator.
        """

        self.user_repository = UserRepository()
        self.status_service = StatusService()
        self.role_service = RoleService()
        self.profile_service = UserProfileService()
        self.email_token_service = EmailTokenService()
        self.email_service = EmailService()

    def authenticate(self, access_token: str):
        """
        Autentifică utilizatorul folosind access token-ul primit de la Google.

        Flow-ul este următorul:
        1. Trimitem token-ul către Google.
        2. Google ne întoarce informațiile utilizatorului.
        3. Verificăm dacă email-ul este de student USV.
        4. Căutăm sau creăm utilizatorul în baza de date.
        5. Dacă este utilizator nou, îi creăm profilul.
        6. Generăm token-urile JWT pentru autentificarea în aplicație.
        """

        try:
            # Trimitem request către Google pentru a obține
            # informațiile utilizatorului asociat token-ului.
            response = requests.get(
                "https://www.googleapis.com/oauth2/v2/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
                timeout=10,
            )

            # Dacă Google nu răspunde cu succes,
            # înseamnă că token-ul este invalid sau expirat.
            if response.status_code != 200:
                return None

            # Convertim răspunsul JSON într-un dicționar Python.
            userinfo = response.json()

            # Extragem email-ul utilizatorului.
            email = userinfo.get("email")

            # Extragem ID-ul unic Google al utilizatorului.
            google_sub = userinfo.get("id")

            # Acceptăm doar email-uri instituționale de student USV.
            if not email or not email.endswith("@student.usv.ro"):
                return None

            # Căutăm utilizatorul după email.
            # Dacă nu există, îl creăm automat.
            user, created = self.user_repository.get_or_create_google_user(email=email)

            # Dacă utilizatorul tocmai a fost creat,
            # trebuie să îi configurăm datele inițiale.
            if created:
                # Setăm o parolă inutilizabilă.
                #
                # Asta înseamnă că utilizatorul nu se poate loga
                # cu parolă clasică, ci doar prin Google.
                user.set_unusable_password()
                user.save()

                # Obținem statusul "Activ" pentru profil.
                status = self.status_service.get_by_name("Activ")

                # Stabilim rolul utilizatorului pe baza email-ului.
                role = self.role_service.assign_role_from_email(email)

                # Creăm profilul utilizatorului.
                self.profile_service.create(
                    user=user,
                    status=status,
                    role=role,
                    google_sub=google_sub,
                    is_google_student=True,
                )

                # Creăm un token pentru completarea profilului.
                token_obj = self.email_token_service.create_token_for_user(user)

                # Trimitem email-ul prin care utilizatorul
                # își poate completa profilul.
                self.email_service.send_complete_profile_email(user, token_obj.token)

            # Obținem profilul utilizatorului.
            profile = self.profile_service.get_by_user_id(user.id)

            # Generăm token-ul JWT refresh pentru utilizator.
            refresh = RefreshToken.for_user(user)

            # Returnăm datele necesare frontend-ului.
            return {
                # Token folosit pentru request-uri autentificate.
                "access": str(refresh.access_token),
                # Token folosit pentru generarea unui access token nou.
                "refresh": str(refresh),
                "user_id": user.id,
                "username": user.username,
                "email": user.email,
                # Dacă profilul nu există, trimitem None.
                # Altfel trimitem datele relevante despre profil.
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
                # Spune frontend-ului dacă userul a fost creat acum
                # sau exista deja în baza de date.
                "created": created,
            }

        except requests.RequestException:
            # Dacă apare o problemă la comunicarea cu Google
            # sau request-ul expiră, autentificarea eșuează.
            return None
