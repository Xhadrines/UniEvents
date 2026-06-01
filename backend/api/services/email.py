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

    def send_registration_confirmation_email(self, user, event, is_waiting_list=False):
        subject = (
            f"Lista de asteptare - {event.name}"
            if is_waiting_list
            else f"Confirmare inscriere - {event.name}"
        )

        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/registration_confirmation_email.html",
            {
                "username": user.username,
                "event": event,
                "is_waiting_list": is_waiting_list,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def send_waiting_list_email(self, user, event):
        subject = f"Lista de asteptare - {event.name}"

        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/waiting_list_email.html",
            {
                "username": user.username,
                "event": event,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def send_registration_cancelled_email(self, user, event):
        subject = f"Inscriere anulata - {event.name}"

        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/registration_cancelled_email.html",
            {
                "username": user.username,
                "event": event,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def send_password_reset_email(self, user, uid, token):
        reset_url = (
            f"http://localhost:2002/reset-password-confirm" f"?uid={uid}&token={token}"
        )

        subject = "Reset password - UniEvents"
        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/password_reset_email.html",
            {
                "username": user.username,
                "reset_url": reset_url,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def send_favorite_event_email(self, user, event):
        subject = f"Eveniment adăugat la favorite - {event.name}"

        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/favorite_event_email.html",
            {
                "username": user.username,
                "event": event,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def send_favorite_event_removed_email(self, user, event):
        subject = f"Eveniment eliminat de la favorite - {event.name}"

        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/favorite_event_removed_email.html",
            {
                "username": user.username,
                "event": event,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def send_admin_role_request_email(self, user, message: str):
        subject = "Cerere rol special - UniEvents"

        from_email = settings.EMAIL_HOST_USER
        to_email = [settings.EMAIL_HOST_USER]

        html_content = render_to_string(
            "emails/admin_role_request_email.html",
            {
                "user": user,
                "message": message,
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)

    def send_welcome_community_email(self, user, role):
        subject = "Bun venit în comunitatea UniEvents"

        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/welcome_community_email.html",
            {
                "username": user.username,
                "first_name": user.first_name,
                "role": role,
                "profile_url": "http://localhost:2002/profile",
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
