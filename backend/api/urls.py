from django.urls import path

from .views import (
    HomeView,
    FacultateView,
    SpecializareView,
    RolView,
    StareView,
    UserView,
    RegisterView,
    LoginView,
    GoogleAuthView,
    UserProfilesView,
    CompleteProfileView,
    TipView,
    OrganizatorView,
    CategorieView,
    TipParticipareView,
    LocatieView,
    EvenimentView,
    SponsorView,
    SponsorEvenimentView,
    InregistrareView,
)


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("facultate/", FacultateView.as_view(), name="facultate"),
    path("facultate/<int:pk>/", FacultateView.as_view(), name="facultate-detail"),
    path("specializare/", SpecializareView.as_view(), name="specializare"),
    path(
        "specializare/<int:pk>/", SpecializareView.as_view(), name="specializare-detail"
    ),
    path("rol/", RolView.as_view(), name="rol"),
    path("rol/<int:pk>/", RolView.as_view(), name="rol-detail"),
    path("stare/", StareView.as_view(), name="stare"),
    path("stare/<int:pk>/", StareView.as_view(), name="stare-detail"),
    path("user/", UserView.as_view(), name="user"),
    path("user/<int:pk>/", UserView.as_view(), name="user-detail"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("auth/google/", GoogleAuthView.as_view(), name="google-auth"),
    path("user_profiles/", UserProfilesView.as_view(), name="user_profiles"),
    path(
        "user_profiles/<int:pk>/",
        UserProfilesView.as_view(),
        name="user_profiles-detail",
    ),
    path("complete-profile/", CompleteProfileView.as_view(), name="complete-profile"),
    path("tip/", TipView.as_view(), name="tip"),
    path("tip/<int:pk>/", TipView.as_view(), name="tip-detail"),
    path("organizator/", OrganizatorView.as_view(), name="organizator"),
    path("organizator/<int:pk>/", OrganizatorView.as_view(), name="organizator-detail"),
    path("categorie/", CategorieView.as_view(), name="categorie"),
    path("categorie/<int:pk>/", CategorieView.as_view(), name="categorie-detail"),
    path("tip_participare/", TipParticipareView.as_view(), name="tip_participare"),
    path(
        "tip_participare/<int:pk>/",
        TipParticipareView.as_view(),
        name="tip_participare-detail",
    ),
    path("locatie/", LocatieView.as_view(), name="locatie"),
    path("locatie/<int:pk>/", LocatieView.as_view(), name="locatie-detail"),
    path("eveniment/", EvenimentView.as_view(), name="eveniment"),
    path("eveniment/<int:pk>/", EvenimentView.as_view(), name="eveniment-detail"),
    path("sponsor/", SponsorView.as_view(), name="sponsor"),
    path("sponsor/<int:pk>/", SponsorView.as_view(), name="sponsor-detail"),
    path(
        "sponsor_eveniment/", SponsorEvenimentView.as_view(), name="sponsor_eveniment"
    ),
    path(
        "sponsor_eveniment/<int:pk>/",
        SponsorEvenimentView.as_view(),
        name="sponsor_eveniment-detail",
    ),
    path("inregistrare/", InregistrareView.as_view(), name="inregistrare"),
    path(
        "inregistrare/<int:pk>/", InregistrareView.as_view(), name="inregistrare-detail"
    ),
]
