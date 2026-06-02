from fileinput import filename

from django.db import models
from django.contrib.auth.models import User

from io import BytesIO
from django.core.files.base import ContentFile

import qrcode

from .base_model import BaseModel
from .organizer import Organizer
from .location import Location
from .category import Category
from .participation_type import ParticipationType
from .status import Status


def event_qr_upload_path(instance, filename):
    """
    Generează calea de upload pentru
    codurile QR ale evenimentelor.

    Structura:
        events/<event_id>/qr_codes/<filename>

    Exemplu:
        events/5/qr_codes/event_5_qr.png
    """

    return f"events/{instance.id}/" f"qr_codes/{filename}"


class Event(BaseModel):
    """
    Model principal pentru evenimentele aplicației.

    Acest model conține:
    - informații generale,
    - organizator,
    - locație,
    - participare,
    - reguli de acces,
    - QR code,
    - validare administrativă.
    """

    # =====================================================
    # BASIC EVENT DATA
    # =====================================================

    # Numele evenimentului.
    name = models.CharField(max_length=150)

    # Descriere completă a evenimentului.
    description = models.TextField()

    # =====================================================
    # LINKS
    # =====================================================

    # Link pentru înscriere.
    #
    # Exemplu:
    # https://example.com/register
    registration_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
    )

    # Link online pentru participare.
    #
    # Exemplu:
    # Google Meet / Zoom / Teams.
    online_link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
    )

    # =====================================================
    # RELATIONS
    # =====================================================

    # Organizatorul evenimentului.
    organizer = models.ForeignKey(
        Organizer,
        on_delete=models.CASCADE,
        related_name="events",
    )

    # Locația evenimentului.
    #
    # PROTECT previne ștergerea locației
    # dacă există evenimente asociate.
    location = models.ForeignKey(
        Location,
        on_delete=models.PROTECT,
        related_name="events",
    )

    # Categoria evenimentului.
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="events",
    )

    # Tip participare:
    # fizic / online / hibrid.
    participation_type = models.ForeignKey(
        ParticipationType,
        on_delete=models.PROTECT,
    )

    # Status eveniment:
    # acceptat, anulat etc.
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )

    # =====================================================
    # EVENT DATES
    # =====================================================

    # Data de început.
    start_date = models.DateTimeField()

    # Data de finalizare.
    end_date = models.DateTimeField()

    # =====================================================
    # REGISTRATION SETTINGS
    # =====================================================

    # Capacitatea maximă.
    #
    # NULL = fără limită.
    capacity = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    # Deadline pentru înscriere.
    registration_deadline = models.DateTimeField(
        null=True,
        blank=True,
    )

    # =====================================================
    # PRICING
    # =====================================================

    # Tip preț:
    # gratuit / plătit.
    pricing_type = models.CharField(
        max_length=10,
        choices=[
            ("free", "Gratuit"),
            ("paid", "Platit"),
        ],
        default="free",
    )

    # =====================================================
    # ACCESS POLICY
    # =====================================================

    # Politica de acces la eveniment.
    #
    # Variante:
    # - open
    # - registration
    # - ticket
    # - registration_ticket
    access_policy = models.CharField(
        max_length=24,
        choices=[
            ("open", "Acces deschis"),
            (
                "registration",
                "Necesita inscriere",
            ),
            (
                "ticket",
                "Necesita bilet",
            ),
            (
                "registration_ticket",
                "Necesita inscriere si bilet",
            ),
        ],
        default="open",
    )

    # =====================================================
    # ACCESS FLAGS
    # =====================================================

    # Eveniment gratuit.
    is_free_entry = models.BooleanField(default=True)

    # Necesită înscriere.
    requires_registration = models.BooleanField(default=False)

    # Necesită bilet.
    requires_ticket = models.BooleanField(default=False)

    # =====================================================
    # QR CODE
    # =====================================================

    # Cod QR generat automat pentru
    # link-ul de înscriere.
    qr_code = models.ImageField(
        upload_to=event_qr_upload_path,
        null=True,
        blank=True,
    )

    # =====================================================
    # MATERIAL LIMITS
    # =====================================================

    # Număr maxim de fișiere asociate.
    max_files = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    # Dimensiune maximă fișier în MB.
    max_file_size_mb = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    # =====================================================
    # VALIDATION
    # =====================================================

    # Administratorul care a validat
    # evenimentul.
    validated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="validated_events",
    )

    # Data validării.
    validated_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    # =====================================================
    # CUSTOM SAVE
    # =====================================================

    def save(self, *args, **kwargs):
        """
        Salvează evenimentul și generează automat
        codul QR dacă:
        - nu există deja,
        - există registration_link.
        """

        # Salvăm inițial obiectul.
        super().save(*args, **kwargs)

        # Generăm QR code doar dacă:
        # - nu există deja,
        # - există link de înscriere.
        if not self.qr_code and self.registration_link:

            # Generăm imaginea QR.
            qr = qrcode.make(self.registration_link)

            # Buffer temporar în memorie.
            buffer = BytesIO()

            # Salvăm imaginea în buffer.
            qr.save(buffer, format="PNG")

            # Numele fișierului QR.
            filename = f"event_{self.id}_qr.png"

            # Salvăm imaginea QR.
            self.qr_code.save(
                filename,
                ContentFile(buffer.getvalue()),
                save=False,
            )

            # Salvăm doar câmpul qr_code.
            super().save(update_fields=["qr_code"])

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a evenimentului.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "events"

        # Ordonare implicită:
        # evenimentele cele mai apropiate primele.
        ordering = ["start_date"]
