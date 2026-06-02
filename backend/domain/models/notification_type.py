from django.db import models

from .base_model import BaseModel


class NotificationType(BaseModel):
    """
    Model utilizat pentru tipurile de notificări
    din aplicație.

    Tipurile de notificări permit clasificarea
    notificărilor trimise utilizatorilor.

    Exemple:
    - reminder,
    - confirmare înscriere,
    - modificare eveniment,
    - anulare eveniment.
    """

    # =====================================================
    # NOTIFICATION TYPE DATA
    # =====================================================

    # Numele tipului de notificare.
    #
    # Exemple:
    # - Reminder
    # - Registration Confirmation
    # - Event Update
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    # Descriere opțională a tipului.
    #
    # Utilizată pentru documentare
    # și administrare.
    description = models.TextField(blank=True)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a tipului
        de notificare.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "notification_types"
