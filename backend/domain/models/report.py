from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel


class Report(BaseModel):
    # Rapoarte generate de administrator
    generated_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to="reports/", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.title}"

    class Meta:
        db_table = "reports"
