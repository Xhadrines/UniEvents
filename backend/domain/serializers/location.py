from ..models import Location

from .base_serializer import BaseSerializer


class LocationSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Location.

    Acest serializer permite:
    - serializarea locațiilor,
    - transformarea obiectelor Location în JSON,
    - validarea datelor primite din request,
    - utilizarea locațiilor în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Location

        # Câmpurile expuse în API.
        fields = [
            "id",
            "name",
            "address",
            "building",
            "room",
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
