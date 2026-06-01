from django.utils import timezone

from .base_service import BaseService
from ..repository import EventRepository


class EventService(BaseService):
    def __init__(self):
        super().__init__(EventRepository())

    def get_upcoming_events(self):
        # Returneaza evenimentele viitoare
        return self.repository.get_upcoming_events()

    def get_by_category(self, category_id: int):
        return self.repository.get_by_category(category_id)

    def get_by_organizer(self, organizer_id: int):
        return self.repository.get_by_organizer(organizer_id)

    def get_by_location(self, location_id: int):
        return self.repository.get_by_location(location_id)

    def get_by_participation_type(self, participation_type_id: int):
        return self.repository.get_by_participation_type(participation_type_id)

    def validate_event(
        self,
        event_id: int,
        admin_user,
        accepted_status,
        max_files=None,
        max_file_size_mb=None,
    ):
        # Marcheaza evenimentul ca validat de administrator
        event = self.repository.get_by_id(event_id)

        if not event:
            return None

        if max_files is not None:
            event.max_files = max_files

        if max_file_size_mb is not None:
            event.max_file_size_mb = max_file_size_mb

        event.status = accepted_status
        event.validated_by = admin_user
        event.validated_at = timezone.now()
        event.save()

        return event

    def cancel_event(self, event_id: int, cancelled_status):
        # Anuleaza un eveniment
        event = self.repository.get_by_id(event_id)

        if not event:
            return None

        event.status = cancelled_status
        event.save()

        return event

    def get_accepted_events(self):
        return self.repository.get_accepted_events()
