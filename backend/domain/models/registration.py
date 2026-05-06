from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .event import Event
from .status import Status


class Registration(BaseModel):
    # Nu folosim OneToOneField, deoarece un user se poate inscrie la mai multe evenimente
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="registrations"
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="registrations"
    )
    status = models.ForeignKey(Status, on_delete=models.PROTECT)

    confirmation_email_sent = models.BooleanField(default=False)
    ticket_qr_code = models.ImageField(
        upload_to="tickets/qr_codes/", null=True, blank=True
    )

    checked_in = models.BooleanField(default=False)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.event.name}"

    class Meta:
        db_table = "registrations"
        unique_together = ("user", "event")
