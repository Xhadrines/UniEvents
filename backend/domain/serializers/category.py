from ..models import Category

from .base_serializer import BaseSerializer


class CategorySerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Category.

    Acest serializer permite:
    - serializarea categoriilor,
    - validarea datelor primite,
    - transformarea obiectelor Category în JSON,
    - transformarea datelor JSON în obiecte Category.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Category

        # Câmpurile expuse în API.
        fields = [
            "id",
            "name",
            "description",
            "created_at",
            "updated_at",
        ]

        # Câmpuri read-only:
        # nu pot fi modificate prin request.
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
