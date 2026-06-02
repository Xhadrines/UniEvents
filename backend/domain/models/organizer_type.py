from django.db import models

from .base_model import BaseModel


class OrganizerType(BaseModel):
    """
    Model utilizat pentru tipurile
    de organizatori ai evenimentelor.

    Exemple:
    - asociație studențească,
    - profesor,
    - club universitar,
    - partener extern,
    - instituție publică.
    """

    # =====================================================
    # ORGANIZER TYPE DATA
    # =====================================================

    # Numele tipului de organizator.
    #
    # Exemple:
    # - Asociatie de studenti
    # - Profesor
    # - Partener extern
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    # Descriere opțională.
    #
    # Oferă informații suplimentare
    # despre rolul organizatorului.
    description = models.TextField(blank=True)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a tipului
        de organizator.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "organizer_types"
