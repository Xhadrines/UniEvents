from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .event import Event
from .status import Status


def registration_ticket_qr_upload_path(
    instance,
    filename,
):
    """
    Generează calea de upload pentru
    codurile QR ale biletelor.

    Structura:
        events/<event_id>/tickets/qr_codes/<filename>

    Exemplu:
        events/5/tickets/qr_codes/user_1.png
    """

    return f"events/{instance.event.id}/" f"tickets/qr_codes/{filename}"


class Registration(BaseModel):
    """
    Model utilizat pentru înscrierile
    utilizatorilor la evenimente.

    Acest model gestionează:
    - participarea la evenimente,
    - lista de așteptare,
    - biletele QR,
    - check-in-ul participanților,
    - confirmările prin email.
    """

    # =====================================================
    # RELATIONS
    # =====================================================

    # Utilizatorul înscris la eveniment.
    #
    # Nu folosim OneToOneField deoarece:
    # - un utilizator se poate înscrie
    #   la mai multe evenimente.
    #
    # Dacă utilizatorul este șters,
    # înscrierile sale sunt eliminate automat.
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="registrations",
    )

    # Evenimentul asociat înscrierii.
    #
    # Dacă evenimentul este șters,
    # înscrierile asociate sunt eliminate.
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="registrations",
    )

    # Status înscriere:
    # - acceptat,
    # - anulat,
    # - lista de așteptare etc.
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )

    # =====================================================
    # EMAIL CONFIRMATION
    # =====================================================

    # Specifică dacă email-ul de confirmare
    # a fost trimis utilizatorului.
    confirmation_email_sent = models.BooleanField(default=False)

    # =====================================================
    # TICKET QR CODE
    # =====================================================

    # Cod QR asociat biletului participantului.
    #
    # Utilizat pentru:
    # - validare acces,
    # - check-in,
    # - scanare la intrare.
    ticket_qr_code = models.ImageField(
        upload_to=registration_ticket_qr_upload_path,
        null=True,
        blank=True,
    )

    # =====================================================
    # CHECK-IN
    # =====================================================

    # Specifică dacă participantul
    # a fost validat la intrare.
    checked_in = models.BooleanField(default=False)

    # Data și ora check-in-ului.
    checked_in_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a înscrierii.
        """

        return f"{self.user.username} - " f"{self.event.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "registrations"

        # Un utilizator se poate înscrie
        # o singură dată la același eveniment.
        unique_together = (
            "user",
            "event",
        )
