from ..models import Sponsor

from .base_serializer import BaseSerializer


class SponsorSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Sponsor.

    Acest serializer permite:
    - serializarea sponsorilor,
    - transformarea obiectelor Sponsor în JSON,
    - validarea datelor primite din request,
    - gestionarea sponsorilor și a logo-urilor în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Sponsor

        # Câmpurile expuse în API.
        fields = [
            "id",
            "name",
            "description",
            "link",
            "logo",
            "status",
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
