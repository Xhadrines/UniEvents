from django.db import models

from .base_model import BaseModel
from .faculty import Faculty


class Specialization(BaseModel):
    name = models.CharField(max_length=150)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.CASCADE, related_name="specializations"
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "specializations"
        unique_together = ("name", "faculty")
