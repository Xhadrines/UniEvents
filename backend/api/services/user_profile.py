from .base_service import BaseService

from ..repository import (
    UserProfileRepository,
    FacultyRepository,
    SpecializationRepository,
    UserRepository,
)

from domain.serializers import UserProfileSerializer


class UserProfileService(BaseService):
    """
    Service responsabil pentru gestionarea profilului utilizatorului.

    Acest service gestionează:
    - obținerea profilului,
    - completarea profilului,
    - actualizarea profilului,
    - datele necesare formularului de profil.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu repository-urile necesare.

        Folosim:
        - UserProfileRepository pentru profil,
        - FacultyRepository pentru facultăți,
        - SpecializationRepository pentru specializări.
        """

        super().__init__(UserProfileRepository())

        self.faculty_repository = FacultyRepository()
        self.specialization_repository = SpecializationRepository()

    def get_by_user_id(self, user_id: int):
        """
        Returnează profilul asociat utilizatorului.
        """

        return self.repository.get_by_user(user_id)

    def get_profile_data(self, user):
        """
        Returnează profilul serializat al utilizatorului.

        Serializer-ul transformă obiectul Django
        într-un format JSON ușor de trimis către frontend.
        """

        # Căutăm profilul utilizatorului.
        profile = self.repository.get_by_user(user.id)

        # Serializăm profilul.
        serializer = UserProfileSerializer(profile)

        # Dacă profilul există -> returnăm datele serializate.
        # Dacă nu există -> returnăm None.
        return serializer.data if profile else None

    def complete_profile(self, user, data):
        """
        Creează sau actualizează profilul utilizatorului.

        Folosit de obicei după:
        - autentificarea prin Google,
        - primul login,
        - completarea informațiilor lipsă.
        """

        # Căutăm profilul existent.
        profile = self.repository.get_by_user(user.id)

        # Facem o copie a datelor pentru a evita
        # modificarea obiectului original.
        clean_data = data.copy()

        # Eliminăm token-ul deoarece nu face parte
        # din modelul profilului.
        clean_data.pop("token", None)

        # Adăugăm ID-ul utilizatorului în date.
        clean_data["user"] = user.id

        # Extragem prenumele și numele separat,
        # deoarece acestea aparțin modelului User,
        # nu UserProfile.
        first_name = clean_data.pop("first_name", None)
        last_name = clean_data.pop("last_name", None)

        # Actualizăm prenumele dacă există.
        if first_name is not None:
            user.first_name = first_name

        # Actualizăm numele dacă există.
        if last_name is not None:
            user.last_name = last_name

        # Salvăm modificările utilizatorului.
        user.save()

        # Dacă profilul există deja,
        # facem update parțial.
        if profile:
            serializer = UserProfileSerializer(
                profile,
                data=clean_data,
                partial=True,
            )

        # Dacă profilul nu există,
        # creăm unul nou.
        else:
            serializer = UserProfileSerializer(data=clean_data)

        # Validăm datele.
        #
        # raise_exception=True:
        # dacă datele sunt invalide,
        # serializer-ul aruncă excepție automat.
        serializer.is_valid(raise_exception=True)

        # Salvăm profilul.
        profile = serializer.save()

        # Returnăm profilul serializat actualizat.
        return UserProfileSerializer(profile).data

    def get_faculties_and_specializations(self):
        """
        Returnează toate facultățile și specializările.

        Aceste date sunt folosite pentru:
        - dropdown-uri,
        - formulare,
        - selectarea facultății și specializării.
        """

        # Obținem toate facultățile.
        faculties = self.faculty_repository.get_all()

        # Obținem toate specializările.
        specializations = self.specialization_repository.get_all()

        # Construim răspunsul pentru frontend.
        return {
            "faculties": [
                {"id": faculty.id, "name": faculty.name} for faculty in faculties
            ],
            "specializations": [
                {
                    "id": specialization.id,
                    "name": specialization.name,
                    # Facultatea de care aparține specializarea.
                    "faculty": specialization.faculty_id,
                }
                for specialization in specializations
            ],
        }

    def update_my_profile(self, user, data):
        """
        Actualizează profilul utilizatorului autentificat.

        Se actualizează:
        - datele din modelul User,
        - și datele din UserProfile.
        """

        user_repository = UserRepository()

        # Extragem datele utilizatorului.
        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        # Verificăm dacă username-ul nou există deja
        # la alt utilizator.
        if username and username != user.username:

            if user_repository.username_exists_for_other_user(username, user.id):
                raise ValueError("Acest username este deja folosit.")

        # Actualizăm datele utilizatorului.
        user = user_repository.update_profile_fields(
            user=user,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        # Obținem profilul utilizatorului.
        profile = self.get_by_user_id(user.id)

        # Dacă profilul nu există,
        # aruncăm eroare.
        if not profile:
            raise ValueError("Profilul nu a fost găsit.")

        profile_data = {}

        # Lista câmpurilor permise pentru actualizare.
        allowed_profile_fields = [
            "faculty",
            "specialization",
            "study_year",
            "group",
            "semi_group",
        ]

        # Extragem doar câmpurile permise.
        for field in allowed_profile_fields:

            if field in data:
                profile_data[field] = data.get(field)

        # Dacă există date pentru profil,
        # actualizăm profilul.
        if profile_data:

            serializer = UserProfileSerializer(
                profile,
                data=profile_data,
                partial=True,
            )

            # Validăm datele.
            serializer.is_valid(raise_exception=True)

            # Salvăm modificările.
            profile = serializer.save()

        # Returnăm utilizatorul și profilul actualizat.
        return {
            "user": user,
            "profile": profile,
        }
