from django.db import models

from .base_model import BaseModel


class OrganizerType(BaseModel):
    # Exemple: asociatie studenti, profesor, club, partener
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "organizer_types"
