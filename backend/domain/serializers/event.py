from ..models import Event

from .base_serializer import BaseSerializer
from .organizer import OrganizerSerializer
from .location import LocationSerializer
from .category import CategorySerializer
from .participation_type import ParticipationTypeSerializer
from .status import StatusSerializer
from .faculty import FacultySerializer
from rest_framework import serializers


class EventSerializer(BaseSerializer):
    organizer = OrganizerSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    participation_type = ParticipationTypeSerializer(read_only=True)
    status = StatusSerializer(read_only=True)
    faculty = FacultySerializer(read_only=True, source="organizer.faculty")
    registered_count = serializers.SerializerMethodField()
    user_registration_status = serializers.SerializerMethodField()
    pricing_type_display = serializers.SerializerMethodField()
    access_policy_display = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "description",
            "registration_link",
            "online_link",
            "organizer",
            "faculty",
            "location",
            "category",
            "participation_type",
            "status",
            "start_date",
            "end_date",
            "capacity",
            "registered_count",
            "user_registration_status",
            "registration_deadline",
            "pricing_type",
            "access_policy",
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
            "pricing_type_display",
            "access_policy_display",
        ]
        read_only_fields = [
            "id",
            "validated_by",
            "validated_at",
            "created_at",
            "updated_at",
        ]

    def _normalize_access_fields(self, attrs):
        data = dict(attrs)
        instance = getattr(self, "instance", None)

        current_is_free = (
            data.get("is_free_entry")
            if "is_free_entry" in data
            else getattr(instance, "is_free_entry", True)
        )
        current_requires_registration = (
            data.get("requires_registration")
            if "requires_registration" in data
            else getattr(instance, "requires_registration", False)
        )
        current_requires_ticket = (
            data.get("requires_ticket")
            if "requires_ticket" in data
            else getattr(instance, "requires_ticket", False)
        )

        pricing_type = data.get("pricing_type")
        if pricing_type is None:
            pricing_type = "free" if current_is_free else "paid"

        access_policy = data.get("access_policy")
        if access_policy is None:
            if current_requires_registration and current_requires_ticket:
                access_policy = "registration_ticket"
            elif current_requires_registration:
                access_policy = "registration"
            elif current_requires_ticket:
                access_policy = "ticket"
            else:
                access_policy = "open"

        data["pricing_type"] = pricing_type
        data["access_policy"] = access_policy
        data["is_free_entry"] = pricing_type == "free"
        data["requires_registration"] = access_policy in (
            "registration",
            "registration_ticket",
        )
        data["requires_ticket"] = access_policy in (
            "ticket",
            "registration_ticket",
        )
        return data

    def validate(self, attrs):
        return self._normalize_access_fields(attrs)

    def get_pricing_type_display(self, obj: Event) -> str:
        return obj.get_pricing_type_display()

    def get_access_policy_display(self, obj: Event) -> str:
        return obj.get_access_policy_display()

    def get_registered_count(self, obj: Event) -> int:
        # count related registrations (could be optimized with annotation)
        try:
            return obj.registrations.count()
        except AttributeError:
            return 0

    def get_user_registration_status(self, obj: Event):
        request = self.context.get("request")

        if not request or not request.user.is_authenticated:
            return None

        registration = (
            obj.registrations.filter(user=request.user).select_related("status").first()
        )

        if not registration or not registration.status:
            return None

        return registration.status.name
