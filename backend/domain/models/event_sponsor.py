from django.db import models

from .base_model import BaseModel
from .sponsor import Sponsor
from .event import Event


class EventSponsor(BaseModel):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.sponsor.name} - {self.event.name}"

    class Meta:
        db_table = "event_sponsors"
        unique_together = ("sponsor", "event")
