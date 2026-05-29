from rest_framework import serializers

from ..models import Feedback

from .base_serializer import BaseSerializer


class FeedbackSerializer(BaseSerializer):
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = Feedback
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
