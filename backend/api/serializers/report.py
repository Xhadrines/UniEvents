from ..models import Report

from .base_serializer import BaseSerializer


class ReportSerializer(BaseSerializer):
    class Meta:
        model = Report
        fields = [
            "id",
            "generated_by",
            "title",
            "description",
            "file",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
