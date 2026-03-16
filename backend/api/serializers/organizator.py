from rest_framework import serializers

from ..models import Organizator


class OrganizatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organizator
        fields = [
            "id",
            "nume",
            "descriere",
            "link",
            "tip",
            "user",
            "stare",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
