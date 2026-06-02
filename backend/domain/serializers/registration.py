from rest_framework import serializers

from ..models import Registration

from .base_serializer import BaseSerializer


class RegistrationSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Registration.

    Acest serializer permite:
    - serializarea înscrierilor la evenimente,
    - afișarea informațiilor despre utilizator,
    - afișarea statusului înscrierii,
    - gestionarea check-in-ului,
    - transformarea obiectelor Registration în JSON.
    """

    # =====================================================
    # EXTRA READ-ONLY FIELDS
    # =====================================================

    # Numele statusului înscrierii.
    #
    # Exemplu:
    # - Acceptat
    # - Lista de asteptare
    status_name = serializers.CharField(
        source="status.name",
        read_only=True,
    )

    # Username-ul utilizatorului înscris.
    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    # Email-ul utilizatorului înscris.
    email = serializers.EmailField(
        source="user.email",
        read_only=True,
    )

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Registration

        # Câmpurile expuse în API.
        fields = [
            "id",
            "user",
            "event",
            "status",
            "status_name",
            "username",
            "email",
            "confirmation_email_sent",
            "ticket_qr_code",
            "checked_in",
            "checked_in_at",
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
