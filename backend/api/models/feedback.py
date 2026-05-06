from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

from .base_model import BaseModel
from .event import Event


class Feedback(BaseModel):
    # Feedback-ul este permis dupa eveniment
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="feedbacks")

    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField(blank=True)

    sentiment_score = models.FloatField(null=True, blank=True)
    sentiment_label = models.CharField(max_length=50, blank=True)

    def __str__(self) -> str:
        return f"{self.event.name} - {self.rating}/5"

    class Meta:
        db_table = "feedbacks"
        unique_together = ("user", "event")
