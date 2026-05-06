from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .event import Event
from .notification_type import NotificationType


class Notification(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications"
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True, blank=True)

    notification_type = models.ForeignKey(NotificationType, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    message = models.TextField()

    scheduled_at = models.DateTimeField(null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    is_read = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        db_table = "notifications"
