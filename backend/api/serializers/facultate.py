from rest_framework import serializers

from ..models import Facultate


class FacultateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facultate
        fields = ["id", "nume", "created_at", "updated_at"]
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
