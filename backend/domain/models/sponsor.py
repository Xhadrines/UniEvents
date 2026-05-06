from django.db import models

from .base_model import BaseModel
from .status import Status


class Sponsor(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to="sponsors/logos/", null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "sponsors"
