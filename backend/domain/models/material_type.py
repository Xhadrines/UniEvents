from django.db import models

from .base_model import BaseModel


class MaterialType(BaseModel):
    """
    Model utilizat pentru tipurile de materiale
    asociate evenimentelor.

    Exemple:
    - PDF,
    - prezentare,
    - imagine,
    - document,
    - arhivă.
    """

    # =====================================================
    # MATERIAL TYPE DATA
    # =====================================================

    # Numele tipului de material.
    #
    # Exemple:
    # - PDF
    # - Presentation
    # - Image
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    # Descriere opțională a tipului.
    #
    # Poate conține informații suplimentare
    # despre utilizarea materialului.
    description = models.TextField(blank=True)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a tipului de material.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "material_types"
