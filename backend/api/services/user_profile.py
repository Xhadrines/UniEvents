from .base_service import BaseService

from ..repository import (
    UserProfileRepository,
    FacultyRepository,
    SpecializationRepository,
)

from domain.serializers import UserProfileSerializer


class UserProfileService(BaseService):
    def __init__(self):
        super().__init__(UserProfileRepository())
        self.faculty_repository = FacultyRepository()
        self.specialization_repository = SpecializationRepository()

    def get_by_user_id(self, user_id: int):
        return self.repository.get_by_user(user_id)

    def get_profile_data(self, user):
        # Returneaza profilul serializat al utilizatorului
        profile = self.repository.get_by_user(user.id)
        serializer = UserProfileSerializer(profile)
        return serializer.data if profile else None

    def complete_profile(self, user, data):
        # Creeaza sau actualizeaza profilul utilizatorului
        profile = self.repository.get_by_user(user.id)

        clean_data = data.copy()
        clean_data.pop("token", None)
        clean_data["user"] = user.id

        first_name = clean_data.pop("first_name", None)
        last_name = clean_data.pop("last_name", None)

        if first_name is not None:
            user.first_name = first_name

        if last_name is not None:
            user.last_name = last_name

        user.save()

        if profile:
            serializer = UserProfileSerializer(
                profile,
                data=clean_data,
                partial=True,
            )
        else:
            serializer = UserProfileSerializer(data=clean_data)

        serializer.is_valid(raise_exception=True)
        profile = serializer.save()

        return UserProfileSerializer(profile).data

    def get_faculties_and_specializations(self):
        # Returneaza facultatile si specializarile pentru formularul de profil
        faculties = self.faculty_repository.get_all()
        specializations = self.specialization_repository.get_all()

        return {
            "faculties": [
                {"id": faculty.id, "name": faculty.name} for faculty in faculties
            ],
            "specializations": [
                {
                    "id": specialization.id,
                    "name": specialization.name,
                    "faculty": specialization.faculty_id,
                }
                for specialization in specializations
            ],
        }
