from django.db import models

from .base_model import BaseModel


class NotificationType(BaseModel):
    # Exemple: reminder, confirmare, modificare eveniment
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "notification_types"
