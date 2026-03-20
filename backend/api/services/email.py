from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


class EmailService:
    def send_complete_profile_email(self, user, token):
        complete_profile_url = f"http://localhost:2002/complete-profile?token={token}"

        subject = "Completează-ți profilul - UniEvents"
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/complete_profile_email.html",
            {"username": user.username, "complete_profile_url": complete_profile_url},
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
