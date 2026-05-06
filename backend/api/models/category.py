from django.db import models

from .base_model import BaseModel


class Category(BaseModel):
    # Tabel folosit pentru categoriile evenimentelor
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "categories"
