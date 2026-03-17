from django.apps import AppConfig
from django.db.models.signals import post_migrate


class ApiConfig(AppConfig):
    name = "api"

    def ready(self):
        from .default_data import insert_default_data

        post_migrate.connect(insert_default_data, sender=self)
