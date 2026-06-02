from ..models import EventMaterial

from .base_serializer import BaseSerializer
from .material_type import MaterialTypeSerializer


class EventMaterialSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul EventMaterial.

    Acest serializer permite:
    - serializarea materialelor evenimentelor,
    - afișarea tipului materialului,
    - transformarea obiectelor în JSON,
    - gestionarea fișierelor asociate evenimentelor.
    """

    # =====================================================
    # NESTED SERIALIZERS
    # =====================================================

    # Serializer nested pentru tipul materialului.
    #
    # Este read-only deoarece:
    # - afișăm datele complete,
    # - relația este gestionată separat.
    material_type = MaterialTypeSerializer(read_only=True)

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = EventMaterial

        # Câmpurile expuse în API.
        fields = [
            "id",
            "event",
            "material_type",
            "title",
            "file",
            "is_public",
            "uploaded_by",
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
