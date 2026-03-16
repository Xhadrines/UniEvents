from rest_framework import serializers

from ..models import TipParticipare


class TipParticipareSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipParticipare
        fields = ["id", "nume", "descriere", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
