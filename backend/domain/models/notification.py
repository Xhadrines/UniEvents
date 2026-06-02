from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .event import Event
from .notification_type import NotificationType


class Notification(BaseModel):
    """
    Model utilizat pentru notificările
    trimise utilizatorilor aplicației.

    Notificările sunt folosite pentru:
    - remindere evenimente,
    - confirmări înscriere,
    - modificări evenimente,
    - anulări,
    - actualizări importante.
    """

    # =====================================================
    # RELATIONS
    # =====================================================

    # Utilizatorul care primește notificarea.
    #
    # Dacă utilizatorul este șters,
    # notificările sale sunt eliminate automat.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    # Evenimentul asociat notificării.
    #
    # Poate fi NULL pentru notificări generale.
    #
    # Dacă evenimentul este șters,
    # notificarea este eliminată automat.
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # Tipul notificării.
    #
    # Exemple:
    # - reminder,
    # - confirmation,
    # - update.
    notification_type = models.ForeignKey(
        NotificationType,
        on_delete=models.PROTECT,
    )

    # =====================================================
    # NOTIFICATION CONTENT
    # =====================================================

    # Titlul notificării.
    title = models.CharField(max_length=150)

    # Mesajul notificării.
    message = models.TextField()

    # =====================================================
    # DELIVERY INFORMATION
    # =====================================================

    # Data programată pentru trimitere.
    #
    # NULL = notificare imediată.
    scheduled_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    # Data la care notificarea a fost trimisă.
    sent_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    # Specifică dacă utilizatorul
    # a citit notificarea.
    is_read = models.BooleanField(default=False)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a notificării.
        """

        return f"{self.title}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "notifications"
