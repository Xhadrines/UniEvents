from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


class EmailService:
    """
    Service responsabil pentru trimiterea emailurilor aplicației.

    Acest service centralizează toată logica legată de email-uri:
    - confirmări,
    - notificări,
    - resetare parolă,
    - favorite,
    - cereri speciale,
    - email-uri de bun venit.

    Avantaj:
    Dacă vrem să modificăm modul în care trimitem email-uri,
    facem schimbările într-un singur loc.
    """

    def send_complete_profile_email(self, user, token):
        """
        Trimite email-ul pentru completarea profilului.

        Utilizatorul primește un link cu token unic
        pentru completarea informațiilor lipsă.
        """

        # Construim URL-ul care conține token-ul utilizatorului.
        complete_profile_url = f"http://localhost:2002/complete-profile?token={token}"

        # Subiectul email-ului.
        subject = "Complete your profile - UniEvents"

        # Email-ul de pe care se trimite mesajul.
        from_email = settings.EMAIL_HOST_USER

        # Lista destinatarilor.
        to_email = [user.email]

        # Generăm conținutul HTML folosind template-ul.
        # render_to_string încarcă fișierul HTML și înlocuiește variabilele.
        html_content = render_to_string(
            "emails/complete_profile_email.html",
            {
                "username": user.username,
                "complete_profile_url": complete_profile_url,
            },
        )

        # Construim email-ul.
        msg = EmailMultiAlternatives(subject, "", from_email, to_email)

        # Atașăm varianta HTML.
        msg.attach_alternative(html_content, "text/html")

        # Trimitem email-ul.
        #
        # fail_silently=False:
        # dacă apare eroare, Django va arunca excepție.
        msg.send(fail_silently=False)

    def send_registration_confirmation_email(self, user, event, is_waiting_list=False):
        """
        Trimite email de confirmare pentru înscriere la eveniment.

        Dacă utilizatorul este pe lista de așteptare,
        subiectul email-ului se modifică automat.
        """

        # Alegem subiectul în funcție de situație.
        subject = (
            f"Lista de asteptare - {event.name}"
            if is_waiting_list
            else f"Confirmare inscriere - {event.name}"
        )

        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        # Generăm template-ul HTML.
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
        """
        Trimite email atunci când utilizatorul este adăugat
        pe lista de așteptare a unui eveniment.
        """

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
        """
        Trimite email atunci când utilizatorul își anulează
        înscrierea la un eveniment.
        """

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
        """
        Trimite email pentru resetarea parolei.

        Email-ul conține:
        - uid-ul utilizatorului,
        - token-ul de resetare.
        """

        # Construim link-ul pentru resetarea parolei.
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
        """
        Trimite email atunci când un eveniment
        este adăugat la favorite.
        """

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
        """
        Trimite email atunci când un eveniment
        este eliminat din favorite.
        """

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
        """
        Trimite email către administrator
        pentru cerere de rol special.

        Exemplu:
        - organizator,
        - administrator,
        - moderator.
        """

        subject = "Cerere rol special - UniEvents"

        from_email = settings.EMAIL_HOST_USER

        # Trimitem email-ul către administratorul aplicației.
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
        """
        Trimite email de bun venit în comunitatea UniEvents.

        Email-ul este trimis după înregistrare
        sau după activarea contului.
        """

        subject = "Bun venit în comunitatea UniEvents"

        from_email = settings.EMAIL_HOST_USER
        to_email = [user.email]

        html_content = render_to_string(
            "emails/welcome_community_email.html",
            {
                "username": user.username,
                "first_name": user.first_name,
                "role": role,
                # Link către profilul utilizatorului.
                "profile_url": "http://localhost:2002/profile",
            },
        )

        msg = EmailMultiAlternatives(subject, "", from_email, to_email)
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
