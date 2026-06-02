from ..models import EventSponsor

from .base_serializer import BaseSerializer


class EventSponsorSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul EventSponsor.

    Acest serializer permite:
    - serializarea relației sponsor-eveniment,
    - transformarea obiectelor în JSON,
    - gestionarea sponsorilor asociați
      evenimentelor.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = EventSponsor

        # Câmpurile expuse în API.
        fields = [
            "id",
            "sponsor",
            "event",
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
