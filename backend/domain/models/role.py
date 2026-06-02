from django.db import models

from .base_model import BaseModel


class Role(BaseModel):
    """
    Model utilizat pentru rolurile
    utilizatorilor din platformă.

    Rolurile controlează:
    - permisiunile,
    - accesul la funcționalități,
    - nivelul de administrare,
    - acțiunile disponibile în sistem.

    Exemple:
    - Administrator,
    - Student,
    - Profesor,
    - Organizatie,
    - Partener.
    """

    # =====================================================
    # ROLE DATA
    # =====================================================

    # Numele rolului.
    #
    # Trebuie să fie unic în aplicație.
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    # Descriere opțională.
    #
    # Oferă informații suplimentare
    # despre responsabilitățile și
    # permisiunile rolului.
    description = models.TextField(blank=True)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a rolului.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "roles"
