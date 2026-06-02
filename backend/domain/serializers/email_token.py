from ..models import EmailToken

from .base_serializer import BaseSerializer


class EmailTokenSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul EmailToken.

    Acest serializer permite:
    - serializarea token-urilor email,
    - validarea datelor,
    - transformarea obiectelor EmailToken în JSON,
    - utilizarea token-urilor în fluxurile
      de verificare și completare profil.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = EmailToken

        # Câmpurile expuse în API.
        fields = [
            "id",
            "user",
            "token",
            "is_used",
            "created_at",
            "updated_at",
        ]

        # Câmpuri read-only:
        # nu pot fi modificate direct prin request.
        read_only_fields = [
            "id",
            "token",
            "created_at",
            "updated_at",
        ]
