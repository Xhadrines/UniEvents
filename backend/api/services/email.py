from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailService:
    # Service pentru trimiterea emailurilor

    def send_complete_profile_email(self, user, token):
        complete_profile_url = f"http://localhost:2002/complete-profile?token={token}"

        subject = "Complete your profile - UniEvents"
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/complete_profile_email.html",
            {
                "username": user.username,
                "complete_profile_url": complete_profile_url,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def send_registration_confirmation_email(self, user, event):
        # Trimite confirmarea inscrierii la eveniment
        subject = f"Registration confirmed - {event.name}"
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/registration_confirmation_email.html",
            {
                "username": user.username,
                "event": event,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
