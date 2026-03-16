from django.db import models

from .sponsor import Sponsor
from .eveniment import Eveniment


class SponsorEveniment(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.CASCADE)
    eveniment = models.ForeignKey(Eveniment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.sponsor.nume} - {self.eveniment.nume}"

    class Meta:
        db_table = "sponsor_event"
