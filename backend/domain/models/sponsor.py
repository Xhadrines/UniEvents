from django.db import models

from .base_model import BaseModel
from .status import Status


def sponsor_logo_upload_path(instance, filename):
    """
    Generează calea de upload pentru
    logo-urile sponsorilor.

    Structura:
        sponsors/<sponsor_id>/logos/<filename>

    Exemplu:
        sponsors/3/logos/logo.png
    """

    return f"sponsors/{instance.id}/" f"logos/{filename}"


class Sponsor(BaseModel):
    """
    Model utilizat pentru sponsorii
    evenimentelor din aplicație.

    Sponsorii pot fi:
    - companii IT,
    - instituții,
    - organizații,
    - parteneri educaționali,
    - sponsori financiari.
    """

    # =====================================================
    # SPONSOR DATA
    # =====================================================

    # Numele sponsorului.
    name = models.CharField(max_length=150)

    # Descriere opțională.
    #
    # Poate conține:
    # - informații despre companie,
    # - domeniul de activitate,
    # - parteneriate,
    # - contribuții.
    description = models.TextField(blank=True)

    # Link extern:
    # website oficial, pagină social media etc.
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
    )

    # Logo-ul sponsorului.
    #
    # Fișier imagine asociat sponsorului.
    logo = models.ImageField(
        upload_to=sponsor_logo_upload_path,
        null=True,
        blank=True,
    )

    # =====================================================
    # STATUS
    # =====================================================

    # Status sponsor:
    # activ, inactiv etc.
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a sponsorului.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "sponsors"
