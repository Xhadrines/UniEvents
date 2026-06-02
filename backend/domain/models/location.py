from django.db import models

from .base_model import BaseModel


class Location(BaseModel):
    """
    Model utilizat pentru locațiile
    asociate evenimentelor.

    Locațiile pot reprezenta:
    - săli,
    - laboratoare,
    - amfiteatre,
    - clădiri,
    - locații externe,
    - locații online.
    """

    # =====================================================
    # LOCATION DATA
    # =====================================================

    # Numele locației.
    #
    # Exemple:
    # - Aula Magna
    # - Laborator AI
    # - Online - Google Meet
    name = models.CharField(max_length=100)

    # Adresa completă a locației.
    address = models.CharField(max_length=255)

    # Clădirea asociată locației.
    #
    # Exemplu:
    # Corp E
    building = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    # Sala / camera locației.
    #
    # Exemplu:
    # Sala 201
    room = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a locației.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "locations"
