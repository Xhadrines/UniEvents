from ..models import Specialization

from .base_serializer import BaseSerializer


class SpecializationSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Specialization.

    Acest serializer permite:
    - serializarea specializărilor,
    - transformarea obiectelor Specialization în JSON,
    - validarea datelor primite din request,
    - utilizarea specializărilor în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Specialization

        # Câmpurile expuse în API.
        fields = [
            "id",
            "name",
            "faculty",
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
