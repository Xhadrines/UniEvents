from rest_framework import serializers

from ..models import Eveniment


class EvenimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eveniment
        fields = [
            "id",
            "nume",
            "descriere",
            "link",
            "organizator",
            "locatie",
            "categorie",
            "tip_participare",
            "start_data",
            "end_data",
            "capacitate",
            "stare",
            "created_at",
            "updated_at",
        ]
        read_only_fields = (
            "id",
            "created_at",
            "updated_at",
        )
