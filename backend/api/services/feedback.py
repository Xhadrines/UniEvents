from django.utils import timezone

from .base_service import BaseService
from ..repository import FeedbackRepository


class FeedbackService(BaseService):
    def __init__(self):
        super().__init__(FeedbackRepository())

    def get_by_event(self, event_id: int):
        return self.repository.get_by_event(event_id)

    def get_by_user(self, user_id: int):
        return self.repository.get_by_user(user_id)

    def create_feedback(self, user, event, rating: int, comment: str = ""):
        # Feedback-ul este permis doar dupa terminarea evenimentului
        if timezone.now() < event.end_date:
            raise ValueError("Feedback can be added only after the event has ended")

        existing_feedback = self.repository.get_by_user_and_event(user.id, event.id)

        if existing_feedback:
            raise ValueError("User already added feedback for this event")

        return self.repository.create(
            user=user,
            event=event,
            rating=rating,
            comment=comment,
        )
