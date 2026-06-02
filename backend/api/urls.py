from django.urls import path

from .views import (
    HomeView,
    FacultyView,
    SpecializationView,
    RoleView,
    AdminRoleRequestView,
    StatusView,
    UserView,
    RegisterView,
    LoginView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
    GoogleAuthView,
    UserProfileView,
    CompleteProfileView,
    MyProfileUpdateView,
    OrganizerTypeView,
    OrganizerView,
    CategoryView,
    ParticipationTypeView,
    LocationView,
    EventView,
    UpcomingEventsView,
    ValidateEventView,
    CancelEventView,
    AcceptedEventsView,
    RejectEventView,
    SponsorView,
    EventSponsorView,
    RegistrationView,
    RegisterToEventView,
    CancelRegistrationView,
    CheckInView,
    FeedbackView,
    AddFeedbackView,
    EventFeedbackListView,
    MaterialTypeView,
    EventMaterialView,
    EventMaterialsByEventView,
    UploadEventMaterialView,
    FavoriteEventView,
    MyFavoriteEventsView,
    AddFavoriteEventView,
    RemoveFavoriteEventView,
    NotificationTypeView,
    NotificationView,
    MyNotificationsView,
    UnreadNotificationsView,
    MarkNotificationAsReadView,
    ReportView,
    EmailTokenView,
)

# Lista tuturor rutelor (URL-urilor) disponibile în API.
#
# urlpatterns:
# - este variabila specială folosită de Django
# - pentru maparea URL-urilor către view-uri.
urlpatterns = [
    # =====================================================
    # HOME
    # =====================================================
    # Pagina principală a aplicației/API-ului.
    path("", HomeView.as_view(), name="home"),
    # =====================================================
    # FACULTIES
    # =====================================================
    # Returnează toate facultățile sau creează una nouă.
    path("faculties/", FacultyView.as_view(), name="faculty"),
    # Returnează o facultate după ID.
    path("faculties/<int:pk>/", FacultyView.as_view(), name="faculty-detail"),
    # =====================================================
    # SPECIALIZATIONS
    # =====================================================
    # Returnează toate specializările.
    path("specializations/", SpecializationView.as_view(), name="specialization"),
    # Returnează o specializare după ID.
    path(
        "specializations/<int:pk>/",
        SpecializationView.as_view(),
        name="specialization-detail",
    ),
    # =====================================================
    # ROLES
    # =====================================================
    # CRUD pentru roluri.
    path("roles/", RoleView.as_view(), name="role"),
    # Detalii rol după ID.
    path("roles/<int:pk>/", RoleView.as_view(), name="role-detail"),
    # Cerere pentru rol administrator.
    path(
        "admin-role-request/",
        AdminRoleRequestView.as_view(),
        name="admin-role-request",
    ),
    # =====================================================
    # STATUSES
    # =====================================================
    # CRUD pentru statusuri.
    path("statuses/", StatusView.as_view(), name="status"),
    # Detalii status după ID.
    path("statuses/<int:pk>/", StatusView.as_view(), name="status-detail"),
    # =====================================================
    # USERS
    # =====================================================
    # CRUD utilizatori.
    path("users/", UserView.as_view(), name="user"),
    # Detalii utilizator după ID.
    path("users/<int:pk>/", UserView.as_view(), name="user-detail"),
    # Înregistrare utilizator.
    path("register/", RegisterView.as_view(), name="register"),
    # Login utilizator.
    path("login/", LoginView.as_view(), name="login"),
    # Cerere resetare parolă.
    path("password-reset/", PasswordResetRequestView.as_view(), name="password-reset"),
    # Confirmare resetare parolă.
    path(
        "password-reset-confirm/",
        PasswordResetConfirmView.as_view(),
        name="password-reset-confirm",
    ),
    # Login prin Google OAuth.
    path("auth/google/", GoogleAuthView.as_view(), name="google-auth"),
    # =====================================================
    # USER PROFILES
    # =====================================================
    # CRUD profile utilizatori.
    path("user-profiles/", UserProfileView.as_view(), name="user-profile"),
    # Detalii profil după ID.
    path(
        "user-profiles/<int:pk>/", UserProfileView.as_view(), name="user-profile-detail"
    ),
    # Completare profil.
    path("complete-profile/", CompleteProfileView.as_view(), name="complete-profile"),
    # Actualizare profil propriu.
    path("my-profile/update/", MyProfileUpdateView.as_view(), name="my-profile-update"),
    # =====================================================
    # ORGANIZER TYPES
    # =====================================================
    # CRUD tipuri organizatori.
    path("organizer-types/", OrganizerTypeView.as_view(), name="organizer-type"),
    # Detalii tip organizator.
    path(
        "organizer-types/<int:pk>/",
        OrganizerTypeView.as_view(),
        name="organizer-type-detail",
    ),
    # =====================================================
    # ORGANIZERS
    # =====================================================
    # CRUD organizatori.
    path("organizers/", OrganizerView.as_view(), name="organizer"),
    # Detalii organizator.
    path("organizers/<int:pk>/", OrganizerView.as_view(), name="organizer-detail"),
    # =====================================================
    # CATEGORIES
    # =====================================================
    # CRUD categorii.
    path("categories/", CategoryView.as_view(), name="category"),
    # Detalii categorie.
    path("categories/<int:pk>/", CategoryView.as_view(), name="category-detail"),
    # =====================================================
    # PARTICIPATION TYPES
    # =====================================================
    # CRUD tipuri participare.
    path(
        "participation-types/",
        ParticipationTypeView.as_view(),
        name="participation-type",
    ),
    # Detalii tip participare.
    path(
        "participation-types/<int:pk>/",
        ParticipationTypeView.as_view(),
        name="participation-type-detail",
    ),
    # =====================================================
    # LOCATIONS
    # =====================================================
    # CRUD locații.
    path("locations/", LocationView.as_view(), name="location"),
    # Detalii locație.
    path("locations/<int:pk>/", LocationView.as_view(), name="location-detail"),
    # =====================================================
    # EVENTS
    # =====================================================
    # CRUD evenimente.
    path("events/", EventView.as_view(), name="event"),
    # Detalii eveniment.
    path("events/<int:pk>/", EventView.as_view(), name="event-detail"),
    # Evenimente viitoare.
    path("events/upcoming/", UpcomingEventsView.as_view(), name="event-upcoming"),
    # Validare eveniment.
    path(
        "events/<int:pk>/validate/", ValidateEventView.as_view(), name="event-validate"
    ),
    # Anulare eveniment.
    path("events/<int:pk>/cancel/", CancelEventView.as_view(), name="event-cancel"),
    # Respingere eveniment.
    path("events/<int:pk>/reject/", RejectEventView.as_view(), name="event-reject"),
    # Returnează doar evenimentele acceptate.
    path(
        "events/accepted/",
        AcceptedEventsView.as_view(),
        name="accepted-events",
    ),
    # =====================================================
    # SPONSORS
    # =====================================================
    # CRUD sponsori.
    path("sponsors/", SponsorView.as_view(), name="sponsor"),
    # Detalii sponsor.
    path("sponsors/<int:pk>/", SponsorView.as_view(), name="sponsor-detail"),
    # =====================================================
    # EVENT SPONSORS
    # =====================================================
    # CRUD relații event-sponsor.
    path("event-sponsors/", EventSponsorView.as_view(), name="event-sponsor"),
    # Detalii relație event-sponsor.
    path(
        "event-sponsors/<int:pk>/",
        EventSponsorView.as_view(),
        name="event-sponsor-detail",
    ),
    # =====================================================
    # REGISTRATIONS
    # =====================================================
    # CRUD înscrieri.
    path("registrations/", RegistrationView.as_view(), name="registration"),
    # Detalii înscriere.
    path(
        "registrations/<int:pk>/",
        RegistrationView.as_view(),
        name="registration-detail",
    ),
    # Înscriere la eveniment.
    path(
        "events/<int:event_id>/register/",
        RegisterToEventView.as_view(),
        name="event-register",
    ),
    # Anulare înscriere.
    path(
        "events/<int:event_id>/cancel-registration/",
        CancelRegistrationView.as_view(),
        name="event-cancel-registration",
    ),
    # Check-in participant.
    path(
        "registrations/<int:registration_id>/check-in/",
        CheckInView.as_view(),
        name="registration-check-in",
    ),
    # =====================================================
    # FEEDBACKS
    # =====================================================
    # CRUD feedback-uri.
    path("feedbacks/", FeedbackView.as_view(), name="feedback"),
    # Detalii feedback.
    path("feedbacks/<int:pk>/", FeedbackView.as_view(), name="feedback-detail"),
    # Adaugă feedback pentru eveniment.
    path(
        "events/<int:event_id>/feedback/",
        AddFeedbackView.as_view(),
        name="event-feedback",
    ),
    # Lista feedback-uri eveniment.
    path(
        "events/<int:event_id>/feedbacks/",
        EventFeedbackListView.as_view(),
        name="event-feedback-list",
    ),
    # =====================================================
    # MATERIAL TYPES
    # =====================================================
    # CRUD tipuri materiale.
    path("material-types/", MaterialTypeView.as_view(), name="material-type"),
    # Detalii tip material.
    path(
        "material-types/<int:pk>/",
        MaterialTypeView.as_view(),
        name="material-type-detail",
    ),
    # =====================================================
    # EVENT MATERIALS
    # =====================================================
    # CRUD materiale evenimente.
    path("event-materials/", EventMaterialView.as_view(), name="event-material"),
    # Detalii material eveniment.
    path(
        "event-materials/<int:pk>/",
        EventMaterialView.as_view(),
        name="event-material-detail",
    ),
    # Materiale după eveniment.
    path(
        "events/<int:event_id>/materials/",
        EventMaterialsByEventView.as_view(),
        name="event-materials-by-event",
    ),
    # Upload material eveniment.
    path(
        "events/<int:event_id>/materials/upload/",
        UploadEventMaterialView.as_view(),
        name="event-material-upload",
    ),
    # =====================================================
    # FAVORITE EVENTS
    # =====================================================
    # CRUD favorite.
    path("favorite-events/", FavoriteEventView.as_view(), name="favorite-event"),
    # Lista favoritelor utilizatorului.
    path(
        "my-favorite-events/",
        MyFavoriteEventsView.as_view(),
        name="my-favorite-events",
    ),
    # Detalii favorit.
    path(
        "favorite-events/<int:pk>/",
        FavoriteEventView.as_view(),
        name="favorite-event-detail",
    ),
    # Adaugă favorit.
    path(
        "events/<int:event_id>/favorite/",
        AddFavoriteEventView.as_view(),
        name="event-favorite-add",
    ),
    # Elimină favorit.
    path(
        "events/<int:event_id>/favorite/remove/",
        RemoveFavoriteEventView.as_view(),
        name="event-favorite-remove",
    ),
    # =====================================================
    # NOTIFICATION TYPES
    # =====================================================
    # CRUD tipuri notificări.
    path(
        "notification-types/", NotificationTypeView.as_view(), name="notification-type"
    ),
    # Detalii tip notificare.
    path(
        "notification-types/<int:pk>/",
        NotificationTypeView.as_view(),
        name="notification-type-detail",
    ),
    # =====================================================
    # NOTIFICATIONS
    # =====================================================
    # CRUD notificări.
    path("notifications/", NotificationView.as_view(), name="notification"),
    # Detalii notificare.
    path(
        "notifications/<int:pk>/",
        NotificationView.as_view(),
        name="notification-detail",
    ),
    # Notificările utilizatorului.
    path("my-notifications/", MyNotificationsView.as_view(), name="my-notifications"),
    # Notificări necitite.
    path(
        "my-notifications/unread/",
        UnreadNotificationsView.as_view(),
        name="unread-notifications",
    ),
    # Marchează notificarea ca citită.
    path(
        "notifications/<int:notification_id>/read/",
        MarkNotificationAsReadView.as_view(),
        name="notification-read",
    ),
    # =====================================================
    # REPORTS
    # =====================================================
    # CRUD rapoarte.
    path("reports/", ReportView.as_view(), name="report"),
    # Detalii raport.
    path("reports/<int:pk>/", ReportView.as_view(), name="report-detail"),
    # =====================================================
    # EMAIL TOKENS
    # =====================================================
    # CRUD token-uri email.
    path("email-tokens/", EmailTokenView.as_view(), name="email-token"),
    # Detalii token email.
    path("email-tokens/<int:pk>/", EmailTokenView.as_view(), name="email-token-detail"),
]
