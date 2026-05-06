from ..models import Feedback

from .base_serializer import BaseSerializer


class FeedbackSerializer(BaseSerializer):
    class Meta:
        model = Feedback
        fields = [
            "id",
            "user",
            "event",
            "rating",
            "comment",
            "sentiment_score",
            "sentiment_label",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "sentiment_score",
            "sentiment_label",
            "created_at",
            "updated_at",
        ]
