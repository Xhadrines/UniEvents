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

    def register_user_to_event(self, user, event, status):
        # Inscrie utilizatorul la eveniment daca nu este deja inscris
        existing_registration = self.repository.get_by_user_and_event(user.id, event.id)

        if existing_registration:
            return existing_registration

        if event.registration_deadline and timezone.now() > event.registration_deadline:
            raise ValueError("Registration deadline has passed")

        return self.repository.create(
            user=user,
            event=event,
            status=status,
        )

    def cancel_registration(self, user_id: int, event_id: int, cancelled_status):
        # Anuleaza inscrierea utilizatorului la eveniment
        registration = self.repository.get_by_user_and_event(user_id, event_id)

        if not registration:
            return None

        registration.status = cancelled_status
        registration.save()

        return registration

    def check_in(self, registration_id: int):
        # Marcheaza participantul ca prezent
        registration = self.repository.get_by_id(registration_id)

        if not registration:
            return None

        registration.checked_in = True
        registration.checked_in_at = timezone.now()
        registration.save()

        return registration
