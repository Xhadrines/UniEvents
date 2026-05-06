from django.db import models

from .base_model import BaseModel


class ParticipationType(BaseModel):
    # Exemple: fizic, online, hibrid
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "participation_types"
