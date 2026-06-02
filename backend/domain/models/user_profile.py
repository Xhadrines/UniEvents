from django.db import models
from django.contrib.auth.models import User

from .base_model import BaseModel
from .faculty import Faculty
from .specialization import Specialization
from .status import Status
from .role import Role


class UserProfile(BaseModel):
    """
    Model utilizat pentru extinderea
    informațiilor utilizatorilor aplicației.

    Acest model extinde tabela implicită:
        auth_user

    și permite stocarea:
    - rolurilor,
    - statusurilor,
    - informațiilor academice,
    - integrării Google OAuth.
    """

    # =====================================================
    # USER RELATION
    # =====================================================

    # Relație one-to-one cu utilizatorul Django.
    #
    # Fiecare utilizator are un singur profil.
    #
    # Dacă utilizatorul este șters,
    # profilul este eliminat automat.
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    # =====================================================
    # STATUS + ROLE
    # =====================================================

    # Status utilizator:
    # activ, inactiv etc.
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
    )

    # Rol utilizator:
    # student, administrator etc.
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
    )

    # =====================================================
    # ACADEMIC INFORMATION
    # =====================================================

    # Facultatea utilizatorului.
    #
    # Poate fi NULL pentru:
    # - parteneri externi,
    # - organizații,
    # - utilizatori generici.
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # Specializarea utilizatorului.
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # =====================================================
    # STUDENT DATA
    # =====================================================

    # Anul de studiu.
    study_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    # Grupa studentului.
    group = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    # Semigrupa studentului.
    #
    # Exemple:
    # - A
    # - B
    semi_group = models.CharField(
        max_length=1,
        null=True,
        blank=True,
    )

    # =====================================================
    # GOOGLE AUTHENTICATION
    # =====================================================

    # Google Subject ID.
    #
    # Utilizat pentru autentificarea
    # prin Google OAuth.
    google_sub = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    # Specifică dacă utilizatorul
    # este autentificat ca student
    # prin Google.
    is_google_student = models.BooleanField(default=False)

    # =====================================================
    # STRING REPRESENTATION
    # =====================================================

    def __str__(self) -> str:
        """
        Reprezentarea text a profilului.
        """

        return f"{self.user.username}"

    # =====================================================
    # DJANGO META CONFIGURATION
    # =====================================================

    class Meta:
        # Numele tabelului din baza de date.
        db_table = "user_profiles"
