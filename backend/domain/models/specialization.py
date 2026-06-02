from django.db import models

from .base_model import BaseModel
from .faculty import Faculty


class Specialization(BaseModel):
    """
    Model utilizat pentru specializările
    asociate facultăților.

    Specializările sunt utilizate pentru:
    - profilurile utilizatorilor,
    - organizarea academică,
    - filtrarea evenimentelor,
    - statistici universitare.

    Exemple:
    - Calculatoare,
    - Automatică,
    - Economie,
    - Drept.
    """

    # =====================================================
    # SPECIALIZATION DATA
    # =====================================================

    # Numele specializării.
    #
    # Exemplu:
    # - Calculatoare
    # - Automatica si Informatica Aplicata
    name = models.CharField(max_length=150)

    # =====================================================
    # RELATIONS
    # =====================================================

    # Facultatea asociată specializării.
    #
    # O facultate poate avea mai multe
    # specializări.
    #
    # Dacă facultatea este ștearsă,
    # specializările asociate sunt eliminate.
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        related_name="specializations",
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a specializării.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "specializations"

        # Previne duplicarea:
        # aceeași specializare nu poate exista
        # de două ori în aceeași facultate.
        unique_together = (
            "name",
            "faculty",
        )
