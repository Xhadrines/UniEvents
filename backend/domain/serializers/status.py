from ..models import Status

from .base_serializer import BaseSerializer


class StatusSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Status.

    Acest serializer permite:
    - serializarea statusurilor din aplicație,
    - transformarea obiectelor Status în JSON,
    - validarea datelor primite din request,
    - utilizarea statusurilor în diverse fluxuri
      (evenimente, utilizatori, notificări etc.).
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Status

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
