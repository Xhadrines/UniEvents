from django.db import models
from django.contrib.auth.models import User
import uuid

from .base_model import BaseModel


class EmailToken(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="email_tokens"
    )
    token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    is_used = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.username} - {self.token}"

    class Meta:
        db_table = "email_tokens"
