from django.utils import timezone

from .base_service import BaseService
from ..repository import RegistrationRepository


class RegistrationService(BaseService):
    def __init__(self):
        super().__init__(RegistrationRepository())

    def get_by_user(self, user_id: int):
        return self.repository.get_by_user(user_id)

    def get_by_event(self, event_id: int):
        return self.repository.get_by_event(event_id)

    def register_user_to_event(self, user, event, accepted_status, waiting_status):
        existing_registration = self.repository.get_by_user_and_event(user.id, event.id)

        if event.registration_deadline and timezone.now() > event.registration_deadline:
            raise ValueError("Registration deadline has passed")

        accepted_count = (
            self.repository.get_by_event(event.id)
            .filter(status=accepted_status)
            .count()
        )

        should_be_waiting = (
            event.capacity is not None and accepted_count >= event.capacity
        )

        if existing_registration:
            if existing_registration.status.name != "Anulat":
                return existing_registration, (
                    existing_registration.status.name == "Lista de asteptare"
                )

            existing_registration.status = (
                waiting_status if should_be_waiting else accepted_status
            )
            existing_registration.save()

            return existing_registration, should_be_waiting

        registration = self.repository.create(
            user=user,
            event=event,
            status=waiting_status if should_be_waiting else accepted_status,
        )

        return registration, should_be_waiting

    def cancel_registration(
        self, user_id: int, event_id: int, cancelled_status, accepted_status=None
    ):
        registration = self.repository.get_by_user_and_event(user_id, event_id)

        if not registration:
            return None, None

        was_accepted = (
            accepted_status is not None and registration.status_id == accepted_status.id
        )

        registration.status = cancelled_status
        registration.save()

        promoted_registration = None

        if was_accepted:
            promoted_registration = (
                self.repository.get_by_event(event_id)
                .filter(status__name="Lista de asteptare")
                .order_by("created_at")
                .first()
            )

            if promoted_registration:
                promoted_registration.status = accepted_status
                promoted_registration.save()

        return registration, promoted_registration

    def check_in(self, registration_id: int):
        # Marcheaza participantul ca prezent
        registration = self.repository.get_by_id(registration_id)

        if not registration:
            return None

        registration.checked_in = True
        registration.checked_in_at = timezone.now()
        registration.save()

        return registration
