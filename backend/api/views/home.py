from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["endpoints"] = [
            ("Facultate", "/api/facultate/"),
            ("Specializare", "/api/specializare/"),
            ("Rol", "/api/rol/"),
            ("Stare", "/api/stare/"),
            ("User", "/api/user/"),
            ("User Profiles", "/api/user_profiles/"),
            ("Tip", "/api/tip/"),
            ("Organizator", "/api/organizator/"),
            ("Categorie", "/api/categorie/"),
            ("Tip Participare", "/api/tip_participare/"),
            ("Locatie", "/api/locatie/"),
            ("Eveniment", "/api/eveniment/"),
            ("Sponsor", "/api/sponsor/"),
            ("Sponsor Eveniment", "/api/sponsor_eveniment/"),
            ("Inregistrare", "/api/inregistrare/"),
        ]

        return context
