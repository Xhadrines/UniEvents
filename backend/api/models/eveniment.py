from django.db import models

from .organizator import Organizator
from .locatie import Locatie
from .categorie import Categorie
from .tip_participare import TipParticipare
from .stare import Stare


class Eveniment(models.Model):
    nume = models.CharField(max_length=150)
    descriere = models.TextField()
    link = models.URLField(max_length=500, blank=True, null=True)
    organizator = models.ForeignKey(Organizator, on_delete=models.CASCADE)
    locatie = models.ForeignKey(Locatie, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    tip_participare = models.ForeignKey(TipParticipare, on_delete=models.CASCADE)
    start_data = models.DateTimeField()
    end_data = models.DateTimeField()
    capacitate = models.IntegerField()
    stare = models.ForeignKey(Stare, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume}"

    class Meta:
        db_table = "events"
