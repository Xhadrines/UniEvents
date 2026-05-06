from .base_service import BaseService

from ..repository import OrganizerRepository


class OrganizerService(BaseService):
    def __init__(self):
        super().__init__(OrganizerRepository())

    def get_by_user(self, user_id: int):
        # Returneaza organizatorul asociat unui user
        return self.repository.get_by_field("user_id", user_id)
