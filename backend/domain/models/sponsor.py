from django.db import models

from .base_model import BaseModel
from .status import Status


def sponsor_logo_upload_path(instance, filename):
    return f"sponsors/{instance.id}/logos/{filename}"


class Sponsor(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=500, blank=True, null=True)
    logo = models.ImageField(upload_to=sponsor_logo_upload_path, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "sponsors"
