from django.apps import AppConfig
from django.db.models.signals import post_migrate


class DomainConfig(AppConfig):
    """
    Configurația aplicației Domain.

    Această aplicație conține:
    - modelele principale ale domeniului,
    - serializer-e,
    - repository logic,
    - semnale pentru inițializarea datelor default.

    La migrarea bazei de date, sunt inserate automat
    datele inițiale (seed data).
    """

    # =====================================================
    # BASIC CONFIG
    # =====================================================

    default_auto_field = "django.db.models.BigAutoField"

    # Numele aplicației Django.
    name = "domain"

    # =====================================================
    # SIGNALS SETUP
    # =====================================================

    def ready(self):
        """
        Rulează la pornirea aplicației.

        Conectează semnalul post_migrate pentru
        inserarea datelor default în baza de date.
        """

        from .signals import insert_default_data

        post_migrate.connect(
            insert_default_data,
            sender=self,
        )
