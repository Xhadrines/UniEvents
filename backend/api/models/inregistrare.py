from django.db import models
from django.contrib.auth.models import User

from .eveniment import Eveniment
from .stare import Stare


class Inregistrare(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    eveniment = models.ForeignKey(Eveniment, on_delete=models.CASCADE)
    stare = models.ForeignKey(Stare, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.eveniment.nume}"

    class Meta:
        db_table = "registrations"
