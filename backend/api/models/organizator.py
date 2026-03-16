from django.db import models
from django.contrib.auth.models import User

from .tip import Tip
from .stare import Stare


class Organizator(models.Model):
    nume = models.CharField(max_length=150)
    descriere = models.TextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    tip = models.ForeignKey(Tip, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stare = models.ForeignKey(Stare, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume}"

    class Meta:
        db_table = "organizers"
