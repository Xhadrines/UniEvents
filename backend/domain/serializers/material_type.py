from ..models import MaterialType

from .base_serializer import BaseSerializer


class MaterialTypeSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul MaterialType.

    Acest serializer permite:
    - serializarea tipurilor de materiale,
    - transformarea obiectelor MaterialType în JSON,
    - validarea datelor primite din request,
    - utilizarea tipurilor de materiale în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = MaterialType

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
