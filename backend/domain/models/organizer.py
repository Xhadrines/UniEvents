from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .organizer_type import OrganizerType
from .status import Status
from .faculty import Faculty


class Organizer(BaseModel):
    """
    Model utilizat pentru organizatorii
    evenimentelor din aplicație.

    Organizatorii pot fi:
    - asociații studențești,
    - profesori,
    - cluburi universitare,
    - parteneri externi,
    - structuri universitare.
    """

    # =====================================================
    # BASIC ORGANIZER DATA
    # =====================================================

    # Numele organizatorului.
    name = models.CharField(max_length=150)

    # Descriere opțională.
    #
    # Poate conține:
    # - informații despre activitate,
    # - scop,
    # - proiecte,
    # - evenimente organizate.
    description = models.TextField(blank=True)

    # Link extern:
    # website, Facebook, Instagram etc.
    link = models.URLField(
        max_length=500,
        blank=True,
        null=True,
    )

    # =====================================================
    # RELATIONS
    # =====================================================

    # Tipul organizatorului.
    #
    # Exemple:
    # - profesor,
    # - organizație,
    # - partener extern.
    organizer_type = models.ForeignKey(
        OrganizerType,
        on_delete=models.PROTECT,
    )

    # Utilizatorul asociat organizatorului.
    #
    # Relație one-to-one:
    # un utilizator poate avea
    # un singur profil de organizator.
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="organizer",
    )

    # Status organizator:
    # activ, inactiv etc.
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )

    # Facultatea asociată organizatorului.
    #
    # Poate fi NULL pentru:
    # - parteneri externi,
    # - organizații independente.
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a organizatorului.
        """

        return f"{self.name}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "organizers"
