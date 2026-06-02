from ..models import Organizer

from .base_serializer import BaseSerializer


class OrganizerSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Organizer.

    Acest serializer permite:
    - serializarea organizatorilor,
    - transformarea obiectelor Organizer în JSON,
    - validarea datelor primite din request,
    - gestionarea organizatorilor în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Organizer

        # Câmpurile expuse în API.
        fields = [
            "id",
            "name",
            "description",
            "link",
            "organizer_type",
            "user",
            "status",
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
