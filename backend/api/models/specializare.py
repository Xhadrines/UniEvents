from django.db import models

from .facultate import Facultate


class Specializare(models.Model):
    nume = models.CharField(max_length=150)
    facultate = models.ForeignKey(Facultate, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume}"

    class Meta:
        db_table = "specializations"
