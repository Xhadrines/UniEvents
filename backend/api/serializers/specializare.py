from rest_framework import serializers

from ..models import Specializare


class SpecializareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specializare
        fields = ["id", "nume", "facultate", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
