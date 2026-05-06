from .base_service import BaseService

from ..repository import EventSponsorRepository


class EventSponsorService(BaseService):
    def __init__(self):
        super().__init__(EventSponsorRepository())

    def get_by_event(self, event_id: int):
        return self.repository.get_by_event(event_id)

    def get_by_sponsor(self, sponsor_id: int):
        return self.repository.get_by_sponsor(sponsor_id)
