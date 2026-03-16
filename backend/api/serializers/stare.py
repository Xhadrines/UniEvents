from rest_framework import serializers

from ..models import Stare


class StareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stare
        fields = ["id", "nume", "descriere", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
