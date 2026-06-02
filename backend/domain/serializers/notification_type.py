from ..models import NotificationType

from .base_serializer import BaseSerializer


class NotificationTypeSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul NotificationType.

    Acest serializer permite:
    - serializarea tipurilor de notificări,
    - transformarea obiectelor NotificationType în JSON,
    - validarea datelor primite din request,
    - utilizarea tipurilor de notificări în API.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = NotificationType

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
