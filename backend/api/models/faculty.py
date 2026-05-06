from django.db import models

from .base_model import BaseModel


class Faculty(BaseModel):
    name = models.CharField(max_length=150, unique=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "faculties"
