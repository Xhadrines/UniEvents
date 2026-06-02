from ..models import Notification

from .base_serializer import BaseSerializer


class NotificationSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Notification.

    Acest serializer permite:
    - serializarea notificărilor,
    - transformarea obiectelor Notification în JSON,
    - afișarea notificărilor în API,
    - gestionarea statusului de citire.
    """

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Notification

        # Câmpurile expuse în API.
        fields = [
            "id",
            "user",
            "event",
            "notification_type",
            "title",
            "message",
            "scheduled_at",
            "sent_at",
            "is_read",
            "created_at",
            "updated_at",
        ]

        # Câmpuri read-only:
        # nu pot fi modificate direct prin request.
        #
        # sent_at este gestionat automat
        # la trimiterea notificării.
        read_only_fields = [
            "id",
            "sent_at",
            "created_at",
            "updated_at",
        ]
