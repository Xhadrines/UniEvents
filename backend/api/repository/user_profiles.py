from .base_repository import BaseRepository

from ..models import UserProfiles, Facultate, Specializare


class UserProfilesRepository(BaseRepository):
    def __init__(self):
        super().__init__(UserProfiles)

    def get_by_user_id(self, user_id):
        return self.model.objects.filter(user_id=user_id).first()

    @staticmethod
    def get_profile_by_user(user):
        return UserProfiles.objects.filter(user=user).first()

    @staticmethod
    def create_or_update_profile(user, data):
        profile, created = UserProfiles.objects.get_or_create(user=user)

        facultate_id = data.get("facultate")
        specializare_id = data.get("specializare")

        profile.facultate = (
            Facultate.objects.get(id=facultate_id) if facultate_id else None
        )
        profile.specializare = (
            Specializare.objects.get(id=specializare_id) if specializare_id else None
        )

        profile.an_studiu = data.get("an_studiu")
        profile.grupa = data.get("grupa")
        profile.semi_grupa = data.get("semi_grupa")
        profile.save()
        return profile

    @staticmethod
    def get_all_faculties():
        return Facultate.objects.all()

    @staticmethod
    def get_all_specializations():
        return Specializare.objects.all()
