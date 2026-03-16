from django.db import models


class Tip(models.Model):
    nume = models.CharField(max_length=50)
    descriere = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nume}"

    class Meta:
        db_table = "types"
