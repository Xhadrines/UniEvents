from rest_framework import serializers

from ..models import Locatie


class LocatieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locatie
        fields = [
            "id",
            "nume",
            "adresa",
            "cladire",
            "camera",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
