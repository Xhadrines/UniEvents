from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel


def report_upload_path(instance, filename):
    """
    Generează calea de upload pentru
    fișierele rapoartelor.

    Structura:
        reports/<report_id>/files/<filename>

    Exemplu:
        reports/3/files/monthly_report.pdf
    """

    return f"reports/{instance.id}/" f"files/{filename}"


class Report(BaseModel):
    """
    Model utilizat pentru rapoartele
    generate în aplicație.

    Rapoartele pot conține:
    - statistici evenimente,
    - participare utilizatori,
    - activitate organizatori,
    - feedback și analize.
    """

    # =====================================================
    # RELATIONS
    # =====================================================

    # Utilizatorul care a generat raportul.
    #
    # De regulă:
    # - administrator,
    # - organizator autorizat.
    #
    # Dacă utilizatorul este șters:
    # - raportul rămâne,
    # - generated_by devine NULL.
    generated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # =====================================================
    # REPORT DATA
    # =====================================================

    # Titlul raportului.
    title = models.CharField(max_length=150)

    # Descriere opțională.
    #
    # Poate conține:
    # - scopul raportului,
    # - perioada analizată,
    # - informații suplimentare.
    description = models.TextField(blank=True)

    # Fișierul raportului.
    #
    # Exemple:
    # - PDF,
    # - Excel,
    # - CSV.
    file = models.FileField(
        upload_to=report_upload_path,
        null=True,
        blank=True,
    )

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a raportului.
        """

        return f"{self.title}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "reports"
