from .base_service import BaseService

from ..repository import (
    UserProfileRepository,
    FacultyRepository,
    SpecializationRepository,
)

from ..serializers import UserProfileSerializer


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

        if profile:
            profile = self.repository.partial_update(profile.id, **data)
        else:
            profile = self.repository.create(user=user, **data)

        serializer = UserProfileSerializer(profile)
        return serializer.data

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
