from .base_service import BaseService

from ..repository import (
    UserProfileRepository,
    FacultyRepository,
    SpecializationRepository,
    UserRepository,
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

    def update_my_profile(self, user, data):
        user_repository = UserRepository()

        username = data.get("username")
        first_name = data.get("first_name")
        last_name = data.get("last_name")

        if username and username != user.username:
            if user_repository.username_exists_for_other_user(username, user.id):
                raise ValueError("Acest username este deja folosit.")

        user = user_repository.update_profile_fields(
            user=user,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        profile = self.get_by_user_id(user.id)

        if not profile:
            raise ValueError("Profilul nu a fost găsit.")

        profile_data = {}

        allowed_profile_fields = [
            "faculty",
            "specialization",
            "study_year",
            "group",
            "semi_group",
        ]

        for field in allowed_profile_fields:
            if field in data:
                profile_data[field] = data.get(field)

        if profile_data:
            serializer = UserProfileSerializer(
                profile,
                data=profile_data,
                partial=True,
            )
            serializer.is_valid(raise_exception=True)
            profile = serializer.save()

        return {
            "user": user,
            "profile": profile,
        }
