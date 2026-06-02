from ..models import FavoriteEvent

from .event import EventSerializer
from .base_serializer import BaseSerializer


class FavoriteEventSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul FavoriteEvent.

    Acest serializer permite:
    - serializarea evenimentelor favorite,
    - afișarea detaliilor complete ale evenimentului,
    - transformarea obiectelor FavoriteEvent în JSON,
    - gestionarea listei de favorite a utilizatorilor.
    """

    # =====================================================
    # NESTED SERIALIZERS
    # =====================================================

    # Serializer nested pentru eveniment.
    #
    # Evenimentul este afișat complet
    # în răspunsul API.
    event = EventSerializer(read_only=True)

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = FavoriteEvent

        # Câmpurile expuse în API.
        fields = [
            "id",
            "user",
            "event",
            "created_at",
            "updated_at",
        ]

        # Câmpuri read-only:
        # nu pot fi modificate direct prin request.
        #
        # user și event sunt gestionate
        # automat în logică.
        read_only_fields = [
            "id",
            "user",
            "event",
            "created_at",
            "updated_at",
        ]
