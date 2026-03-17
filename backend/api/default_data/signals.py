from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from .default_data import (
    default_user_data,
    default_faultate_data,
    default_specializari_data,
    default_rol_data,
    default_stare_data,
    default_user_profiles_data,
    default_tip_data,
    default_organizator_data,
    default_categorie_data,
    default_tip_participare_data,
    default_locatie_data,
    default_eveniment_data,
    default_sponsor_data,
    default_sponsor_eveniment_data,
    default_inregistrare_data,
)


APPS = ["api"]


@receiver(post_migrate)
def insert_default_data(sender, **kwargs):
    app_name = sender.name.split(".")[-1]
    if app_name not in APPS:
        return

    Facultate = apps.get_model(app_name, "Facultate")
    for data in default_faultate_data():
        Facultate.objects.get_or_create(nume=data["nume"], defaults=data)

    Specializare = apps.get_model(app_name, "Specializare")
    for data in default_specializari_data():
        Specializare.objects.get_or_create(nume=data["nume"], defaults=data)

    Rol = apps.get_model(app_name, "Rol")
    for data in default_rol_data():
        Rol.objects.get_or_create(nume=data["nume"], defaults=data)

    Stare = apps.get_model(app_name, "Stare")
    for data in default_stare_data():
        Stare.objects.get_or_create(nume=data["nume"], defaults=data)

    for data in default_user_data():
        data["password"] = make_password(data.pop("password"))
        User.objects.get_or_create(email=data["email"], defaults=data)

    UserProfiles = apps.get_model(app_name, "UserProfiles")
    for data in default_user_profiles_data():
        UserProfiles.objects.get_or_create(user=data["user"], defaults=data)

    Tip = apps.get_model(app_name, "Tip")
    for data in default_tip_data():
        Tip.objects.get_or_create(nume=data["nume"], defaults=data)

    Organizator = apps.get_model(app_name, "Organizator")
    for data in default_organizator_data():
        Organizator.objects.get_or_create(user=data["user"], defaults=data)

    Categorie = apps.get_model(app_name, "Categorie")
    for data in default_categorie_data():
        Categorie.objects.get_or_create(nume=data["nume"], defaults=data)

    TipParticipare = apps.get_model(app_name, "TipParticipare")
    for data in default_tip_participare_data():
        TipParticipare.objects.get_or_create(nume=data["nume"], defaults=data)

    Locatie = apps.get_model(app_name, "Locatie")
    for data in default_locatie_data():
        Locatie.objects.get_or_create(nume=data["nume"], defaults=data)

    Eveniment = apps.get_model(app_name, "Eveniment")
    for data in default_eveniment_data():
        Eveniment.objects.get_or_create(nume=data["nume"], defaults=data)

    Sponsor = apps.get_model(app_name, "Sponsor")
    for data in default_sponsor_data():
        Sponsor.objects.get_or_create(nume=data["nume"], defaults=data)

    SponsorEveniment = apps.get_model(app_name, "SponsorEveniment")
    for data in default_sponsor_eveniment_data():
        SponsorEveniment.objects.get_or_create(
            sponsor=data["sponsor"], eveniment=data["eveniment"], defaults=data
        )

    Inregistrare = apps.get_model(app_name, "Inregistrare")
    for data in default_inregistrare_data():
        Inregistrare.objects.get_or_create(
            user=data["user"], eveniment=data["eveniment"], defaults=data
        )
