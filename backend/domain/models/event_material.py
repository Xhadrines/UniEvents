from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .event import Event
from .material_type import MaterialType


def event_material_upload_path(instance, filename):
    return f"events/{instance.event.id}/materials/{filename}"


class EventMaterial(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="materials")
    material_type = models.ForeignKey(MaterialType, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    file = models.FileField(upload_to=event_material_upload_path)
    is_public = models.BooleanField(default=True)

    uploaded_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        db_table = "event_materials"
