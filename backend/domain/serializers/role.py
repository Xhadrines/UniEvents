from ..models import Role

from .base_serializer import BaseSerializer


class RoleSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Role.

    Acest serializer permite:
    - serializarea rolurilor utilizatorilor,
    - transformarea obiectelor Role în JSON,
    - validarea datelor primite din request,
    - utilizarea rolurilor în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Role

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
