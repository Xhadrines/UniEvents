from fileinput import filename

from django.db import models
from django.contrib.auth.models import User

from io import BytesIO
from django.core.files.base import ContentFile
import qrcode

from .base_model import BaseModel
from .organizer import Organizer
from .location import Location
from .category import Category
from .participation_type import ParticipationType
from .status import Status


def event_qr_upload_path(instance, filename):
    return f"events/{instance.id}/qr_codes/{filename}"


class Event(BaseModel):
    name = models.CharField(max_length=150)
    description = models.TextField()

    registration_link = models.URLField(max_length=500, blank=True, null=True)
    online_link = models.URLField(max_length=500, blank=True, null=True)

    organizer = models.ForeignKey(
        Organizer, on_delete=models.CASCADE, related_name="events"
    )
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, related_name="events"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="events"
    )
    participation_type = models.ForeignKey(ParticipationType, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    capacity = models.PositiveIntegerField(null=True, blank=True)
    registration_deadline = models.DateTimeField(null=True, blank=True)

    pricing_type = models.CharField(
        max_length=10,
        choices=[
            ("free", "Gratuit"),
            ("paid", "Platit"),
        ],
        default="free",
    )
    access_policy = models.CharField(
        max_length=24,
        choices=[
            ("open", "Acces deschis"),
            ("registration", "Necesita inscriere"),
            ("ticket", "Necesita bilet"),
            ("registration_ticket", "Necesita inscriere si bilet"),
        ],
        default="open",
    )

    is_free_entry = models.BooleanField(default=True)
    requires_registration = models.BooleanField(default=False)
    requires_ticket = models.BooleanField(default=False)

    qr_code = models.ImageField(
        upload_to=event_qr_upload_path,
        null=True,
        blank=True,
    )

    max_files = models.PositiveIntegerField(null=True, blank=True)
    max_file_size_mb = models.PositiveIntegerField(null=True, blank=True)

    validated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="validated_events",
    )
    validated_at = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.qr_code and self.registration_link:
            qr = qrcode.make(self.registration_link)
            buffer = BytesIO()
            qr.save(buffer, format="PNG")

            filename = f"event_{self.id}_qr.png"
            self.qr_code.save(filename, ContentFile(buffer.getvalue()), save=False)

            super().save(update_fields=["qr_code"])

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        db_table = "events"
        ordering = ["start_date"]
