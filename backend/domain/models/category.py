from django.db import models

from .base_model import BaseModel


class Category(BaseModel):
    """
    Model utilizat pentru categoriile evenimentelor.

    Categoriile permit organizarea și filtrarea
    evenimentelor din aplicație.

    Exemple:
    - Tehnologie
    - Carieră
    - Educație
    - Sport
    """

    # =====================================================
    # CATEGORY DATA
    # =====================================================

    # Numele categoriei.
    #
    # Trebuie să fie unic în aplicație.
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    # Descriere opțională a categoriei.
    #
    # Poate conține detalii suplimentare
    # despre tipul evenimentelor asociate.
    description = models.TextField(blank=True)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a categoriei.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "categories"
