from ..models import ParticipationType

from .base_serializer import BaseSerializer


class ParticipationTypeSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul ParticipationType.

    Acest serializer permite:
    - serializarea tipurilor de participare,
    - transformarea obiectelor ParticipationType în JSON,
    - validarea datelor primite din request,
    - utilizarea tipurilor de participare în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = ParticipationType

        # Câmpurile expuse în API.
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]

        # Câmpuri read-only:
        # nu pot fi modificate direct prin request.
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
