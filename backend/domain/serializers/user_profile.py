from ..models import UserProfile

from .base_serializer import BaseSerializer


class UserProfileSerializer(BaseSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "id",
            "user",
            "status",
            "role",
            "faculty",
            "specialization",
            "study_year",
            "group",
            "semi_group",
            "google_sub",
            "is_google_student",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "faculty": {"required": False, "allow_null": True},
            "specialization": {"required": False, "allow_null": True},
            "study_year": {"required": False, "allow_null": True},
            "group": {"required": False, "allow_null": True},
            "semi_group": {"required": False, "allow_null": True},
            "google_sub": {"required": False, "allow_null": True},
            "is_google_student": {"required": False},
        }
