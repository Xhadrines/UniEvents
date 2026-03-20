from .base_service import BaseService

from ..serializers import UserProfilesSerializer

from ..repository import UserProfilesRepository


class UserProfilesService(BaseService):
    def __init__(self):
        super().__init__(UserProfilesRepository())

    def get_by_user_id(self, user_id):
        return self.repository.get_by_user_id(user_id)

    @staticmethod
    def get_profile_data(user):
        profile = UserProfilesRepository.get_profile_by_user(user)
        serializer = UserProfilesSerializer(profile)
        return serializer.data if profile else None

    @staticmethod
    def complete_profile(user, data):
        profile = UserProfilesRepository.create_or_update_profile(user, data)
        serializer = UserProfilesSerializer(profile)
        return serializer.data

    @staticmethod
    def get_faculties_and_specializations():
        faculties = UserProfilesRepository.get_all_faculties()
        specializations = UserProfilesRepository.get_all_specializations()
        return {
            "faculties": [{"id": f.id, "name": f.nume} for f in faculties],
            "specializations": [{"id": s.id, "name": s.nume} for s in specializations],
        }
