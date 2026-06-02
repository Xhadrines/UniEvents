from django.db import models

from .base_model import BaseModel


class Faculty(BaseModel):
    """
    Model utilizat pentru facultățile
    din cadrul universității.

    Facultățile sunt asociate cu:
    - specializări,
    - organizatori,
    - profiluri utilizatori,
    - evenimente universitare.
    """

    # =====================================================
    # FACULTY DATA
    # =====================================================

    # Numele facultății.
    #
    # Trebuie să fie unic în aplicație.
    name = models.CharField(
        max_length=150,
        unique=True,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a facultății.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "faculties"
