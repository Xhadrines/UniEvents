from django.apps import apps
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .default_data import (
    default_user_data,
    default_status_data,
    default_role_data,
    default_faculty_data,
    default_specialization_data,
    default_user_profile_data,
    default_organizer_type_data,
    default_organizer_data,
    default_category_data,
    default_participation_type_data,
    default_location_data,
    default_event_data,
    default_sponsor_data,
    default_event_sponsor_data,
    default_registration_data,
    default_feedback_data,
    default_material_type_data,
    default_event_material_data,
    default_favorite_event_data,
    default_notification_type_data,
    default_notification_data,
    default_report_data,
    default_email_token_data,
)

# Aplicațiile pentru care rulează seed-ul automat
APPS = ["domain"]


@receiver(post_migrate)
def insert_default_data(sender, **kwargs):
    """
    Seed automat rulat după migrarea bazei de date.

    Populează inițial toate tabelele cu date default:
    - utilizatori
    - roluri și statusuri
    - structuri academice
    - evenimente
    - notificări
    - feedback etc.
    """

    # Numele aplicației care a declanșat semnalul
    app_name = sender.name.split(".")[-1]

    # Rulează seed doar pentru aplicațiile permise
    if app_name not in APPS:
        return

    # =====================================================
    # STATUS
    # =====================================================

    Status = apps.get_model(app_name, "Status")
    for data in default_status_data():
        Status.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    # =====================================================
    # ROLE
    # =====================================================

    Role = apps.get_model(app_name, "Role")
    for data in default_role_data():
        Role.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    # =====================================================
    # FACULTY + SPECIALIZATION
    # =====================================================

    Faculty = apps.get_model(app_name, "Faculty")
    for data in default_faculty_data():
        Faculty.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    Specialization = apps.get_model(app_name, "Specialization")
    for data in default_specialization_data():
        Specialization.objects.get_or_create(
            name=data["name"],
            faculty=data["faculty"],
            defaults=data,
        )

    # =====================================================
    # USERS
    # =====================================================

    for data in default_user_data():
        password = data.pop("password")

        user, created = User.objects.get_or_create(
            email=data["email"],
            defaults=data,
        )

        if created:
            user.set_password(password)
            user.save()

    # =====================================================
    # USER PROFILE
    # =====================================================

    UserProfile = apps.get_model(app_name, "UserProfile")
    for data in default_user_profile_data():
        UserProfile.objects.get_or_create(
            user=data["user"],
            defaults=data,
        )

    # =====================================================
    # ORGANIZERS
    # =====================================================

    OrganizerType = apps.get_model(app_name, "OrganizerType")
    for data in default_organizer_type_data():
        OrganizerType.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    Organizer = apps.get_model(app_name, "Organizer")
    for data in default_organizer_data():
        Organizer.objects.get_or_create(
            user=data["user"],
            defaults=data,
        )

    # =====================================================
    # EVENT CATALOG STRUCTURE
    # =====================================================

    Category = apps.get_model(app_name, "Category")
    for data in default_category_data():
        Category.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    ParticipationType = apps.get_model(app_name, "ParticipationType")
    for data in default_participation_type_data():
        ParticipationType.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    Location = apps.get_model(app_name, "Location")
    for data in default_location_data():
        Location.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    # =====================================================
    # EVENTS
    # =====================================================

    Event = apps.get_model(app_name, "Event")
    for data in default_event_data():
        Event.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    # =====================================================
    # SPONSORS
    # =====================================================

    Sponsor = apps.get_model(app_name, "Sponsor")
    for data in default_sponsor_data():
        Sponsor.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    EventSponsor = apps.get_model(app_name, "EventSponsor")
    for data in default_event_sponsor_data():
        EventSponsor.objects.get_or_create(
            sponsor=data["sponsor"],
            event=data["event"],
            defaults=data,
        )

    # =====================================================
    # REGISTRATIONS
    # =====================================================

    Registration = apps.get_model(app_name, "Registration")
    for data in default_registration_data():
        Registration.objects.get_or_create(
            user=data["user"],
            event=data["event"],
            defaults=data,
        )

    # =====================================================
    # FEEDBACK
    # =====================================================

    Feedback = apps.get_model(app_name, "Feedback")
    for data in default_feedback_data():
        Feedback.objects.get_or_create(
            user=data["user"],
            event=data["event"],
            defaults=data,
        )

    # =====================================================
    # MATERIALS
    # =====================================================

    MaterialType = apps.get_model(app_name, "MaterialType")
    for data in default_material_type_data():
        MaterialType.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    EventMaterial = apps.get_model(app_name, "EventMaterial")
    for data in default_event_material_data():
        EventMaterial.objects.get_or_create(
            event=data["event"],
            title=data["title"],
            defaults=data,
        )

    # =====================================================
    # FAVORITES
    # =====================================================

    FavoriteEvent = apps.get_model(app_name, "FavoriteEvent")
    for data in default_favorite_event_data():
        FavoriteEvent.objects.get_or_create(
            user=data["user"],
            event=data["event"],
            defaults=data,
        )

    # =====================================================
    # NOTIFICATIONS
    # =====================================================

    NotificationType = apps.get_model(app_name, "NotificationType")
    for data in default_notification_type_data():
        NotificationType.objects.get_or_create(
            name=data["name"],
            defaults=data,
        )

    Notification = apps.get_model(app_name, "Notification")
    for data in default_notification_data():
        Notification.objects.get_or_create(
            user=data["user"],
            title=data["title"],
            defaults=data,
        )

    # =====================================================
    # REPORTS
    # =====================================================

    Report = apps.get_model(app_name, "Report")
    for data in default_report_data():
        Report.objects.get_or_create(
            title=data["title"],
            defaults=data,
        )

    # =====================================================
    # EMAIL TOKENS
    # =====================================================

    EmailToken = apps.get_model(app_name, "EmailToken")
    for data in default_email_token_data():
        EmailToken.objects.get_or_create(
            user=data["user"],
            is_used=data["is_used"],
            defaults=data,
        )
