from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .event import Event


class FavoriteEvent(BaseModel):
    """
    Model utilizat pentru evenimentele favorite
    ale utilizatorilor.

    Permite:
    - salvarea evenimentelor preferate,
    - notificări automate,
    - remindere,
    - recomandări personalizate.
    """

    # =====================================================
    # RELATIONS
    # =====================================================

    # Utilizatorul care a adăugat
    # evenimentul la favorite.
    #
    # Dacă utilizatorul este șters,
    # favoritele sale sunt eliminate automat.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="favorite_events",
    )

    # Evenimentul salvat la favorite.
    #
    # Dacă evenimentul este șters,
    # relația este eliminată automat.
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="favorites",
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a relației
        utilizator-eveniment favorit.
        """

        return f"{self.user.username} - " f"{self.event.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "favorite_events"

        # Previne duplicarea relației:
        # un utilizator nu poate adăuga
        # același eveniment de mai multe ori.
        unique_together = (
            "user",
            "event",
        )
