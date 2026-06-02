from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .event import Event
from .material_type import MaterialType


def event_material_upload_path(instance, filename):
    """
    Generează calea de upload pentru materialele
    asociate evenimentelor.

    Structura rezultată:
        events/<event_id>/materials/<filename>

    Exemplu:
        events/5/materials/slides.pdf
    """

    return f"events/{instance.event.id}/" f"materials/{filename}"


class EventMaterial(BaseModel):
    """
    Model utilizat pentru materialele asociate
    evenimentelor.

    Exemple:
    - PDF-uri,
    - prezentări,
    - imagini,
    - arhive,
    - documentații.
    """

    # =====================================================
    # RELATIONS
    # =====================================================

    # Evenimentul asociat materialului.
    #
    # Dacă evenimentul este șters,
    # materialele asociate sunt eliminate automat.
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="materials",
    )

    # Tipul materialului:
    # PDF, prezentare, imagine etc.
    material_type = models.ForeignKey(
        MaterialType,
        on_delete=models.PROTECT,
    )

    # =====================================================
    # MATERIAL DATA
    # =====================================================

    # Titlul materialului.
    title = models.CharField(max_length=150)

    # Fișierul încărcat.
    #
    # Este salvat automat în directorul
    # generat de funcția:
    # event_material_upload_path
    file = models.FileField(upload_to=event_material_upload_path)

    # Specifică dacă materialul poate fi
    # accesat public de utilizatori.
    is_public = models.BooleanField(default=True)

    # =====================================================
    # USER RELATION
    # =====================================================

    # Utilizatorul care a încărcat materialul.
    #
    # Dacă utilizatorul este șters:
    # - materialul rămâne,
    # - uploaded_by devine NULL.
    uploaded_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a materialului.
        """

        return f"{self.title}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "event_materials"
