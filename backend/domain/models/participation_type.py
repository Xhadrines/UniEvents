from django.db import models

from .base_model import BaseModel


class ParticipationType(BaseModel):
    """
    Model utilizat pentru tipurile
    de participare la evenimente.

    Exemple:
    - fizic,
    - online,
    - hibrid.

    Acest model permite clasificarea
    modului în care participanții
    pot participa la evenimente.
    """

    # =====================================================
    # PARTICIPATION TYPE DATA
    # =====================================================

    # Numele tipului de participare.
    #
    # Exemple:
    # - Fizic
    # - Online
    # - Hibrid
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    # Descriere opțională.
    #
    # Oferă informații suplimentare
    # despre modul de participare.
    description = models.TextField(blank=True)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a tipului
        de participare.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "participation_types"
