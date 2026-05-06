from .base_repository import BaseRepository

from ..models import Feedback


class FeedbackRepository(BaseRepository):
    def __init__(self):
        super().__init__(Feedback)

    def get_by_event(self, event_id: int):
        # Returneaza feedback-ul pentru un eveniment
        return self.model.objects.filter(event_id=event_id)

    def get_by_user(self, user_id: int):
        # Returneaza feedback-ul unui utilizator
        return self.model.objects.filter(user_id=user_id)

    def get_by_user_and_event(self, user_id: int, event_id: int):
        # Returneaza feedback-ul unui utilizator pentru un eveniment
        return self.model.objects.filter(user_id=user_id, event_id=event_id).first()
