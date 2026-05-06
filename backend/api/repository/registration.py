from .base_repository import BaseRepository

from ..models import Registration


class RegistrationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Registration)

    def get_by_user(self, user_id: int):
        # Returneaza inscrierile unui utilizator
        return self.model.objects.filter(user_id=user_id)

    def get_by_event(self, event_id: int):
        # Returneaza inscrierile la un eveniment
        return self.model.objects.filter(event_id=event_id)

    def get_by_user_and_event(self, user_id: int, event_id: int):
        # Returneaza inscrierea unui utilizator la un eveniment
        return self.model.objects.filter(user_id=user_id, event_id=event_id).first()
