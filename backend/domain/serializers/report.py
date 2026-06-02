from ..models import Report

from .base_serializer import BaseSerializer


class ReportSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Report.

    Acest serializer permite:
    - serializarea rapoartelor,
    - transformarea obiectelor Report în JSON,
    - gestionarea fișierelor asociate rapoartelor,
    - afișarea informațiilor administrative.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Report

        # Câmpurile expuse în API.
        fields = [
            "id",
            "generated_by",
            "title",
            "description",
            "file",
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
