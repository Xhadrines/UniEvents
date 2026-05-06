from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .faculty import Faculty
from .specialization import Specialization
from .status import Status
from .role import Role


class UserProfile(BaseModel):
    # Extindem tabela auth_user creata automat de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    role = models.ForeignKey(Role, on_delete=models.PROTECT)

    faculty = models.ForeignKey(
        Faculty, on_delete=models.SET_NULL, null=True, blank=True
    )
    specialization = models.ForeignKey(
        Specialization, on_delete=models.SET_NULL, null=True, blank=True
    )

    study_year = models.PositiveSmallIntegerField(null=True, blank=True)
    group = models.PositiveSmallIntegerField(null=True, blank=True)
    semi_group = models.CharField(max_length=1, null=True, blank=True)

    # Folosit pentru autentificarea Google a studentilor
    google_sub = models.CharField(max_length=255, blank=True, null=True)
    is_google_student = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.user.username}"

    class Meta:
        db_table = "user_profiles"
