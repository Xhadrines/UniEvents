from django.db import models

from .base_model import BaseModel
from .sponsor import Sponsor
from .event import Event


class EventSponsor(BaseModel):
    """
    Model intermediar pentru relația dintre
    sponsori și evenimente.

    Permite asocierea sponsorilor cu
    evenimentele organizate în aplicație.

    Relația este de tip:
        many-to-many

    Un sponsor poate susține mai multe evenimente,
    iar un eveniment poate avea mai mulți sponsori.
    """

    # =====================================================
    # RELATIONS
    # =====================================================

    # Sponsorul asociat evenimentului.
    #
    # Dacă sponsorul este șters,
    # relația este eliminată automat.
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.CASCADE,
    )

    # Evenimentul sponsorizat.
    #
    # Dacă evenimentul este șters,
    # relația este eliminată automat.
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a relației
        sponsor-eveniment.
        """

        return f"{self.sponsor.name} - " f"{self.event.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "event_sponsors"

        # Previne duplicarea relației:
        # același sponsor nu poate fi asociat
        # de mai multe ori aceluiași eveniment.
        unique_together = (
            "sponsor",
            "event",
        )
