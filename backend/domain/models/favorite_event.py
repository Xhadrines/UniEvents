from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .event import Event


class FavoriteEvent(BaseModel):
    # Evenimente salvate pentru notificari si recomandari
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="favorite_events"
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="favorites")

    def __str__(self) -> str:
        return f"{self.user.username} - {self.event.name}"

    class Meta:
        db_table = "favorite_events"
        unique_together = ("user", "event")
