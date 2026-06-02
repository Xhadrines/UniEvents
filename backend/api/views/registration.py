from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import (
    RegistrationService,
    EventService,
    StatusService,
    EmailService,
)
from domain.serializers import RegistrationSerializer


class RegistrationView(BaseCRUDView):
    """
    View CRUD pentru înscrierile la evenimente.

    Moștenește BaseCRUDView,
    deci oferă automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica înscrierilor.
    service = RegistrationService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = RegistrationSerializer


class RegisterToEventView(APIView):
    """
    View responsabil pentru înscrierea utilizatorului
    la un eveniment.
    """

    def post(self, request, event_id):
        """
        Înscrie utilizatorul la eveniment.

        Posibile situații:
        - utilizator acceptat,
        - utilizator pus pe lista de așteptare,
        - deadline expirat,
        - deja înscris.
        """

        registration_service = RegistrationService()
        event_service = EventService()
        status_service = StatusService()
        email_service = EmailService()

        # Căutăm evenimentul.
        event = event_service.get_by_id(event_id)

        # Dacă evenimentul nu există.
        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Obținem statusurile necesare.
        accepted_status = status_service.get_by_name("Acceptat")

        waiting_status = status_service.get_by_name("Lista de asteptare")

        try:
            # Încercăm înscrierea utilizatorului.
            registration, is_waiting_list = registration_service.register_user_to_event(
                user=request.user,
                event=event,
                accepted_status=accepted_status,
                waiting_status=waiting_status,
            )

            # Dacă utilizatorul este pus în waiting list.
            if is_waiting_list:

                # Trimitem email specific pentru lista de așteptare.
                email_service.send_waiting_list_email(
                    request.user,
                    event,
                )

            else:
                # Trimitem email de confirmare înscriere.
                email_service.send_registration_confirmation_email(
                    request.user,
                    event,
                )

            # Returnăm înscrierea creată.
            return Response(
                RegistrationSerializer(registration).data,
                status=status.HTTP_201_CREATED,
            )

        except ValueError as error:
            # Dacă apare eroare de business logic,
            # returnăm mesajul către frontend.
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CancelRegistrationView(APIView):
    """
    View responsabil pentru anularea înscrierii
    la un eveniment.
    """

    def post(self, request, event_id):
        """
        Anulează înscrierea utilizatorului.

        Dacă utilizatorul avea loc confirmat:
        - primul utilizator din waiting list
          este promovat automat.
        """

        service = RegistrationService()
        status_service = StatusService()

        # Obținem statusurile necesare.
        cancelled_status = status_service.get_by_name("Anulat")

        accepted_status = status_service.get_by_name("Acceptat")

        email_service = EmailService()

        # Anulăm înscrierea.
        registration, promoted_registration = service.cancel_registration(
            user_id=request.user.id,
            event_id=event_id,
            cancelled_status=cancelled_status,
            accepted_status=accepted_status,
        )

        # Dacă înscrierea nu există.
        if not registration:
            return Response(
                {"error": "Registration not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Dacă cineva a fost promovat
        # din lista de așteptare.
        if promoted_registration:

            # Trimitem email de confirmare.
            email_service.send_registration_confirmation_email(
                promoted_registration.user,
                promoted_registration.event,
                is_waiting_list=False,
            )

        # Trimitem email de anulare
        # utilizatorului curent.
        email_service.send_registration_cancelled_email(
            request.user,
            registration.event,
        )

        # Returnăm înscrierea actualizată.
        return Response(RegistrationSerializer(registration).data)


class CheckInView(APIView):
    """
    View responsabil pentru check-in-ul participanților.

    Check-in-ul confirmă prezența utilizatorului
    la eveniment.
    """

    def post(self, request, registration_id):
        """
        Marchează participantul ca prezent.
        """

        service = RegistrationService()

        # Realizăm check-in-ul.
        registration = service.check_in(registration_id)

        # Dacă înscrierea nu există.
        if not registration:
            return Response(
                {"error": "Registration not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Returnăm înscrierea actualizată.
        return Response(RegistrationSerializer(registration).data)
