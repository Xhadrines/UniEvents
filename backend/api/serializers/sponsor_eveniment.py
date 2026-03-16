from rest_framework import serializers

from ..models import SponsorEveniment


class SponsorEvenimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorEveniment
        fields = ["id", "sponsor", "eveniment", "created_at", "updated_at"]
        read_only_fields = ["id", "created_at", "updated_at"]
