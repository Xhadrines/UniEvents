from .base_repository import BaseRepository

from ..models import EventSponsor


class EventSponsorRepository(BaseRepository):
    def __init__(self):
        super().__init__(EventSponsor)

    def get_by_event(self, event_id: int):
        # Returneaza sponsorii unui eveniment
        return self.model.objects.filter(event_id=event_id)

    def get_by_sponsor(self, sponsor_id: int):
        # Returneaza evenimentele unui sponsor
        return self.model.objects.filter(sponsor_id=sponsor_id)
