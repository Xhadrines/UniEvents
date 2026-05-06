from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import RegistrationService, EventService, StatusService, EmailService
from ..serializers import RegistrationSerializer


class RegistrationView(BaseCRUDView):
    service = RegistrationService()
    serializer_class = RegistrationSerializer


class RegisterToEventView(APIView):
    def post(self, request, event_id):
        registration_service = RegistrationService()
        event_service = EventService()
        status_service = StatusService()
        email_service = EmailService()

        event = event_service.get_by_id(event_id)

        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        accepted_status = status_service.get_by_name("Acceptat")

        try:
            registration = registration_service.register_user_to_event(
                user=request.user,
                event=event,
                status=accepted_status,
            )

            email_service.send_registration_confirmation_email(request.user, event)

            return Response(
                RegistrationSerializer(registration).data,
                status=status.HTTP_201_CREATED,
            )

        except ValueError as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CancelRegistrationView(APIView):
    def post(self, request, event_id):
        service = RegistrationService()
        status_service = StatusService()

        cancelled_status = status_service.get_by_name("Anulat")

        registration = service.cancel_registration(
            user_id=request.user.id,
            event_id=event_id,
            cancelled_status=cancelled_status,
        )

        if not registration:
            return Response(
                {"error": "Registration not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(RegistrationSerializer(registration).data)


class CheckInView(APIView):
    def post(self, request, registration_id):
        service = RegistrationService()

        registration = service.check_in(registration_id)

        if not registration:
            return Response(
                {"error": "Registration not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(RegistrationSerializer(registration).data)
