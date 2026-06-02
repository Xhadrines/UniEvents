from ..models import Faculty

from .base_serializer import BaseSerializer


class FacultySerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Faculty.

    Acest serializer permite:
    - serializarea facultăților,
    - transformarea obiectelor Faculty în JSON,
    - validarea datelor primite din request,
    - utilizarea facultăților în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Faculty

        # Câmpurile expuse în API.
        fields = [
            "id",
            "name",
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
