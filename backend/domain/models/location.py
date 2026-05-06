from django.db import models

from .base_model import BaseModel


class Location(BaseModel):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    building = models.CharField(max_length=50, blank=True, null=True)
    room = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "locations"
