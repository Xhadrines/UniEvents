from django.apps import AppConfig
from django.db.models.signals import post_migrate

class DomainConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "domain"

    def ready(self):
        from .default_data import insert_default_data

        post_migrate.connect(insert_default_data, sender=self)

        print("DomainConfig loaded and post_migrate connected.")
