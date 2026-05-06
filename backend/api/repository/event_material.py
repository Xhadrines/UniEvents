from .base_repository import BaseRepository

from domain.models import EventMaterial


class EventMaterialRepository(BaseRepository):
    def __init__(self):
        super().__init__(EventMaterial)

    def get_by_event(self, event_id: int):
        # Returneaza materialele unui eveniment
        return self.model.objects.filter(event_id=event_id)
