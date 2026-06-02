from django.db import models

from .base_model import BaseModel


class Status(BaseModel):
    """
    Model general utilizat pentru statusurile
    entităților din aplicație.

    Acest model permite reutilizarea acelorași
    statusuri pentru:
    - evenimente,
    - utilizatori,
    - organizatori,
    - înscrieri,
    - notificări,
    - alte procese administrative.

    Exemple:
    - Activ,
    - Inactiv,
    - Acceptat,
    - Respins,
    - Anulat,
    - Finalizat.
    """

    # =====================================================
    # STATUS DATA
    # =====================================================

    # Numele statusului.
    #
    # Trebuie să fie unic în aplicație.
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    # Descriere opțională.
    #
    # Explică semnificația și utilizarea
    # statusului în sistem.
    description = models.TextField(blank=True)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a statusului.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "statuses"
