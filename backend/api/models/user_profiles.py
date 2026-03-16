from django.db import models
from django.contrib.auth.models import User

from .facultate import Facultate
from .specializare import Specializare
from .stare import Stare
from .rol import Rol


class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stare = models.ForeignKey(Stare, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    facultate = models.ForeignKey(Facultate, on_delete=models.CASCADE)
    specializare = models.ForeignKey(Specializare, on_delete=models.CASCADE)
    an_studiu = models.IntegerField()
    grupa = models.IntegerField()
    semi_grupa = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        db_table = "user_profiles"
