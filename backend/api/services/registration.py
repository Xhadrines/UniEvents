from django.utils import timezone

from .base_service import BaseService
from ..repository import RegistrationRepository


class RegistrationService(BaseService):
    """
    Service responsabil pentru gestionarea înscrierilor la evenimente.

    Acest service gestionează:
    - înscrierea utilizatorilor,
    - anularea înscrierilor,
    - lista de așteptare,
    - check-in-ul participanților.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu RegistrationRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Registration.
        """

        super().__init__(RegistrationRepository())

    def get_by_user(self, user_id: int):
        """
        Returnează toate înscrierile unui utilizator.
        """

        return self.repository.get_by_user(user_id)

    def get_by_event(self, event_id: int):
        """
        Returnează toate înscrierile unui eveniment.
        """

        return self.repository.get_by_event(event_id)

    def register_user_to_event(self, user, event, accepted_status, waiting_status):
        """
        Înscrie utilizatorul la un eveniment.

        Logica implementată:
        - verificăm deadline-ul,
        - verificăm dacă utilizatorul este deja înscris,
        - verificăm capacitatea evenimentului,
        - dacă locurile sunt ocupate -> utilizatorul intră pe lista de așteptare.
        """

        # Verificăm dacă utilizatorul este deja înscris.
        existing_registration = self.repository.get_by_user_and_event(user.id, event.id)

        # Verificăm dacă perioada de înscriere a expirat.
        if event.registration_deadline and timezone.now() > event.registration_deadline:
            raise ValueError("Registration deadline has passed")

        # Numărăm participanții acceptați.
        accepted_count = (
            self.repository.get_by_event(event.id)
            .filter(status=accepted_status)
            .count()
        )

        # Verificăm dacă evenimentul a atins capacitatea maximă.
        should_be_waiting = (
            event.capacity is not None and accepted_count >= event.capacity
        )

        # Dacă utilizatorul este deja înscris.
        if existing_registration:

            # Dacă înscrierea NU este anulată,
            # returnăm înscrierea existentă.
            if existing_registration.status.name != "Anulat":
                return existing_registration, (
                    existing_registration.status.name == "Lista de asteptare"
                )

            # Dacă înscrierea era anulată,
            # o reactivăm.
            existing_registration.status = (
                waiting_status if should_be_waiting else accepted_status
            )

            existing_registration.save()

            return existing_registration, should_be_waiting

        # Creăm înscriere nouă.
        registration = self.repository.create(
            user=user,
            event=event,
            status=(waiting_status if should_be_waiting else accepted_status),
        )

        return registration, should_be_waiting

    def cancel_registration(
        self, user_id: int, event_id: int, cancelled_status, accepted_status=None
    ):
        """
        Anulează înscrierea unui utilizator.

        Dacă utilizatorul avea loc confirmat,
        promovăm automat primul utilizator
        din lista de așteptare.
        """

        # Căutăm înscrierea utilizatorului.
        registration = self.repository.get_by_user_and_event(user_id, event_id)

        # Dacă înscrierea nu există,
        # returnăm None.
        if not registration:
            return None, None

        # Verificăm dacă utilizatorul avea loc acceptat.
        was_accepted = (
            accepted_status is not None and registration.status_id == accepted_status.id
        )

        # Marcăm înscrierea ca anulată.
        registration.status = cancelled_status
        registration.save()

        promoted_registration = None

        # Dacă utilizatorul avea loc confirmat,
        # încercăm să promovăm pe cineva
        # din lista de așteptare.
        if was_accepted:

            # Alegem primul utilizator din waiting list.
            #
            # order_by("created_at"):
            # primul înscris în waiting list
            # va fi promovat primul.
            promoted_registration = (
                self.repository.get_by_event(event_id)
                .filter(status__name="Lista de asteptare")
                .order_by("created_at")
                .first()
            )

            # Dacă există cineva în waiting list,
            # îl promovăm la status acceptat.
            if promoted_registration:
                promoted_registration.status = accepted_status
                promoted_registration.save()

        return registration, promoted_registration

    def check_in(self, registration_id: int):
        """
        Marchează participantul ca prezent la eveniment.

        Check-in-ul este folosit pentru:
        - validarea prezenței,
        - statistici,
        - confirmarea participării.
        """

        # Căutăm înscrierea după ID.
        registration = self.repository.get_by_id(registration_id)

        # Dacă înscrierea nu există,
        # returnăm None.
        if not registration:
            return None

        # Marcăm participantul ca prezent.
        registration.checked_in = True

        # Salvăm momentul check-in-ului.
        registration.checked_in_at = timezone.now()

        # Salvăm modificările.
        registration.save()

        return registration
