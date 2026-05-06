from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .organizer_type import OrganizerType
from .status import Status
from .faculty import Faculty


class Organizer(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    link = models.URLField(max_length=500, blank=True, null=True)

    organizer_type = models.ForeignKey(OrganizerType, on_delete=models.PROTECT)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="organizer"
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    faculty = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "organizers"
