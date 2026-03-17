from rest_framework import serializers

from ..models import UserProfiles


class UserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfiles
        fields = [
            "id",
            "user",
            "stare",
            "rol",
            "facultate",
            "specializare",
            "an_studiu",
            "grupa",
            "semi_grupa",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        extra_kwargs = {
            "facultate": {"required": False},
            "specializare": {"required": False},
            "an_studiu": {"required": False},
            "grupa": {"required": False},
            "semi_grupa": {"required": False},
        }
