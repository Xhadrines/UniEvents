from rest_framework import serializers

from ..models import Feedback

from .base_serializer import BaseSerializer


class FeedbackSerializer(BaseSerializer):
    """
    Serializer utilizat pentru modelul Feedback.

    Acest serializer permite:
    - serializarea feedback-urilor,
    - afișarea username-ului utilizatorului,
    - transformarea obiectelor Feedback în JSON,
    - afișarea analizei de sentiment.
    """

    # =====================================================
    # EXTRA READ-ONLY FIELDS
    # =====================================================

    # Username-ul utilizatorului care
    # a trimis feedback-ul.
    #
    # Este extras automat din:
    # user.username
    username = serializers.CharField(
        source="user.username",
        read_only=True,
    )

    # =====================================================
    # DJANGO REST FRAMEWORK META
    # =====================================================

    class Meta:
        # Modelul asociat serializer-ului.
        model = Feedback

        # Câmpurile expuse în API.
        fields = [
            "id",
            "user",
            "username",
            "event",
            "rating",
            "comment",
            "sentiment_score",
            "sentiment_label",
            "created_at",
            "updated_at",
        ]

        # Câmpuri read-only:
        # nu pot fi modificate direct prin request.
        #
        # sentiment_score și sentiment_label
        # sunt generate automat.
        read_only_fields = [
            "id",
            "user",
            "username",
            "event",
            "sentiment_score",
            "sentiment_label",
            "created_at",
            "updated_at",
        ]
