from ..models import OrganizerType

from .base_serializer import BaseSerializer


class OrganizerTypeSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul OrganizerType.

    Acest serializer permite:
    - serializarea tipurilor de organizatori,
    - transformarea obiectelor OrganizerType în JSON,
    - validarea datelor primite din request,
    - utilizarea tipurilor de organizatori în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = OrganizerType

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
