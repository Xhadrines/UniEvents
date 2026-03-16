from rest_framework import serializers

from ..models import Inregistrare


class InregistrareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inregistrare
        fields = ["id", "user", "eveniment", "stare", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
