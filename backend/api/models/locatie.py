from django.db import models


class Locatie(models.Model):
    nume = models.CharField(max_length=50)
    adresa = models.CharField(max_length=200)
    cladire = models.CharField(max_length=50, blank=True, null=True)
    camera = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume}"

    class Meta:
        db_table = "locations"
