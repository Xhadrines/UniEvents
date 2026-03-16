from rest_framework import serializers

from ..models import Tip


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ["id", "nume", "descriere", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
