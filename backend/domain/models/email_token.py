from django.db import models
from django.contrib.auth.models import User

import uuid

from .base_model import BaseModel


class EmailToken(BaseModel):
    """
    Model utilizat pentru token-urile asociate emailurilor.

    Acest model este folosit pentru:
    - completarea profilului,
    - verificarea identității,
    - activarea contului,
    - fluxuri securizate bazate pe email.
    """

    # =====================================================
    # RELATIONS
    # =====================================================

    # Utilizatorul asociat token-ului.
    #
    # Dacă utilizatorul este șters,
    # token-urile sale sunt eliminate automat.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="email_tokens",
    )

    # =====================================================
    # TOKEN DATA
    # =====================================================

    # Token unic generat automat.
    #
    # Este utilizat pentru:
    # - validare email,
    # - completare profil,
    # - acces temporar securizat.
    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
    )

    # Indică dacă token-ul a fost deja utilizat.
    #
    # Previne reutilizarea token-urilor.
    is_used = models.BooleanField(default=False)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a token-ului.
        """

        return f"{self.user.username} - {self.token}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "email_tokens"
