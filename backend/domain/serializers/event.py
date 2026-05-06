from ..models import Event

from .base_serializer import BaseSerializer


class EventSerializer(BaseSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "description",
            "registration_link",
            "online_link",
            "organizer",
            "location",
            "category",
            "participation_type",
            "status",
            "start_date",
            "end_date",
            "capacity",
            "registration_deadline",
            "is_free_entry",
            "requires_registration",
            "requires_ticket",
            "qr_code",
            "max_files",
            "max_file_size_mb",
            "validated_by",
            "validated_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "validated_by",
            "validated_at",
            "created_at",
            "updated_at",
        ]
