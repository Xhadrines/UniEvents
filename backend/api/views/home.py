from django.views.generic import TemplateView


class HomeView(TemplateView):
    # Pagina principala pentru listarea endpointurilor API
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["endpoints"] = [
            # Home
            ("Home", "/api/"),
            # Authentication
            ("Register", "/api/register/"),
            ("Login", "/api/login/"),
            ("Google Auth", "/api/auth/google/"),
            ("Complete Profile", "/api/complete-profile/"),
            # Users
            ("Users", "/api/users/"),
            ("Users Detail", "/api/users/1/"),
            # User Profiles
            ("User Profiles", "/api/user-profiles/"),
            ("User Profiles Detail", "/api/user-profiles/1/"),
            # Roles
            ("Roles", "/api/roles/"),
            ("Roles Detail", "/api/roles/1/"),
            # Statuses
            ("Statuses", "/api/statuses/"),
            ("Statuses Detail", "/api/statuses/1/"),
            # Faculties
            ("Faculties", "/api/faculties/"),
            ("Faculties Detail", "/api/faculties/1/"),
            # Specializations
            ("Specializations", "/api/specializations/"),
            ("Specializations Detail", "/api/specializations/1/"),
            # Organizer Types
            ("Organizer Types", "/api/organizer-types/"),
            ("Organizer Types Detail", "/api/organizer-types/1/"),
            # Organizers
            ("Organizers", "/api/organizers/"),
            ("Organizers Detail", "/api/organizers/1/"),
            # Categories
            ("Categories", "/api/categories/"),
            ("Categories Detail", "/api/categories/1/"),
            # Participation Types
            ("Participation Types", "/api/participation-types/"),
            ("Participation Types Detail", "/api/participation-types/1/"),
            # Locations
            ("Locations", "/api/locations/"),
            ("Locations Detail", "/api/locations/1/"),
            # Events
            ("Events", "/api/events/"),
            ("Events Detail", "/api/events/1/"),
            ("Upcoming Events", "/api/events/upcoming/"),
            ("Validate Event", "/api/events/1/validate/"),
            ("Cancel Event", "/api/events/1/cancel/"),
            # Sponsors
            ("Sponsors", "/api/sponsors/"),
            ("Sponsors Detail", "/api/sponsors/1/"),
            # Event Sponsors
            ("Event Sponsors", "/api/event-sponsors/"),
            ("Event Sponsors Detail", "/api/event-sponsors/1/"),
            # Registrations
            ("Registrations", "/api/registrations/"),
            ("Registrations Detail", "/api/registrations/1/"),
            ("Register To Event", "/api/events/1/register/"),
            ("Cancel Registration", "/api/events/1/cancel-registration/"),
            ("Check In", "/api/registrations/1/check-in/"),
            # Feedbacks
            ("Feedbacks", "/api/feedbacks/"),
            ("Feedbacks Detail", "/api/feedbacks/1/"),
            ("Add Event Feedback", "/api/events/1/feedback/"),
            # Material Types
            ("Material Types", "/api/material-types/"),
            ("Material Types Detail", "/api/material-types/1/"),
            # Event Materials
            ("Event Materials", "/api/event-materials/"),
            ("Event Materials Detail", "/api/event-materials/1/"),
            ("Event Materials By Event", "/api/events/1/materials/"),
            ("Upload Event Material", "/api/events/1/materials/upload/"),
            # Favorite Events
            ("Favorite Events", "/api/favorite-events/"),
            ("Favorite Events Detail", "/api/favorite-events/1/"),
            ("Add Favorite Event", "/api/events/1/favorite/"),
            ("Remove Favorite Event", "/api/events/1/favorite/remove/"),
            # Notification Types
            ("Notification Types", "/api/notification-types/"),
            ("Notification Types Detail", "/api/notification-types/1/"),
            # Notifications
            ("Notifications", "/api/notifications/"),
            ("Notifications Detail", "/api/notifications/1/"),
            ("My Notifications", "/api/my-notifications/"),
            ("Unread Notifications", "/api/my-notifications/unread/"),
            ("Mark Notification As Read", "/api/notifications/1/read/"),
            # Reports
            ("Reports", "/api/reports/"),
            ("Reports Detail", "/api/reports/1/"),
            # Email Tokens
            ("Email Tokens", "/api/email-tokens/"),
            ("Email Tokens Detail", "/api/email-tokens/1/"),
        ]

        return context
