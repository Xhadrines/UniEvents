from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import EventService, StatusService
from ..serializers import EventSerializer


class EventView(BaseCRUDView):
    service = EventService()
    serializer_class = EventSerializer


class UpcomingEventsView(APIView):
    def get(self, request):
        service = EventService()
        events = service.get_upcoming_events()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class ValidateEventView(APIView):
    def post(self, request, pk):
        service = EventService()
        status_service = StatusService()

        accepted_status = status_service.get_by_name("Acceptat")

        event = service.validate_event(
            event_id=pk,
            admin_user=request.user,
            accepted_status=accepted_status,
        )

        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(EventSerializer(event).data)


class CancelEventView(APIView):
    def post(self, request, pk):
        service = EventService()
        status_service = StatusService()

        cancelled_status = status_service.get_by_name("Anulat")
        event = service.cancel_event(pk, cancelled_status)

        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(EventSerializer(event).data)
