from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import EventService, StatusService
from domain.serializers import EventSerializer


class EventView(BaseCRUDView):
    """
    View CRUD pentru evenimente.

    Moștenește BaseCRUDView,
    deci oferă automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica evenimentelor.
    service = EventService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = EventSerializer


class UpcomingEventsView(APIView):
    """
    View folosit pentru obținerea evenimentelor viitoare.
    """

    def get(self, request):
        """
        Returnează toate evenimentele
        care nu au început încă.
        """

        # Inițializăm service-ul.
        service = EventService()

        # Obținem evenimentele viitoare.
        events = service.get_upcoming_events()

        # Serializăm lista de evenimente.
        serializer = EventSerializer(
            events,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


class ValidateEventView(APIView):
    """
    View folosit pentru validarea/aprobarea unui eveniment.

    Acțiunea este realizată de administrator.
    """

    def post(self, request, pk):
        """
        Validează evenimentul și îl marchează ca acceptat.

        În plus:
        - se pot seta limite pentru fișiere,
        - se salvează administratorul care a validat.
        """

        # Inițializăm service-urile necesare.
        service = EventService()
        status_service = StatusService()

        # Obținem statusul "Acceptat".
        accepted_status = status_service.get_by_name("Acceptat")

        # Obținem limitele pentru fișiere din request.
        max_files = request.data.get("max_files")
        max_file_size_mb = request.data.get("max_file_size_mb")

        # Convertim valorile în integer.
        #
        # Dacă nu există valori -> None.
        max_files = int(max_files) if max_files not in (None, "") else None

        max_file_size_mb = (
            int(max_file_size_mb) if max_file_size_mb not in (None, "") else None
        )

        # Validăm evenimentul.
        event = service.validate_event(
            event_id=pk,
            # Administratorul care aprobă evenimentul.
            admin_user=request.user,
            accepted_status=accepted_status,
            max_files=max_files,
            max_file_size_mb=max_file_size_mb,
        )

        # Dacă evenimentul nu există.
        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Returnăm evenimentul actualizat.
        return Response(
            EventSerializer(
                event,
                context={"request": request},
            ).data
        )


class CancelEventView(APIView):
    """
    View folosit pentru anularea unui eveniment.
    """

    def post(self, request, pk):
        """
        Marchează evenimentul ca anulat.
        """

        service = EventService()
        status_service = StatusService()

        # Obținem statusul "Anulat".
        cancelled_status = status_service.get_by_name("Anulat")

        # Anulăm evenimentul.
        event = service.cancel_event(pk, cancelled_status)

        # Dacă evenimentul nu există.
        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Returnăm evenimentul actualizat.
        return Response(
            EventSerializer(
                event,
                context={"request": request},
            ).data
        )


class RejectEventView(APIView):
    """
    View folosit pentru respingerea unui eveniment.

    Diferența față de anulare:
    - evenimentul este respins înainte de aprobare.
    """

    def post(self, request, pk):
        """
        Marchează evenimentul ca respins.
        """

        service = EventService()
        status_service = StatusService()

        # Obținem statusul "Respins".
        rejected_status = status_service.get_by_name("Respins")

        # Folosim aceeași logică precum la anulare,
        # doar că schimbăm statusul.
        event = service.cancel_event(pk, rejected_status)

        # Dacă evenimentul nu există.
        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Returnăm evenimentul actualizat.
        return Response(
            EventSerializer(
                event,
                context={"request": request},
            ).data
        )


class AcceptedEventsView(APIView):
    """
    View folosit pentru obținerea
    evenimentelor aprobate/acceptate.
    """

    def get(self, request):
        """
        Returnează doar evenimentele
        care au statusul "Acceptat".
        """

        service = EventService()

        # Obținem evenimentele acceptate.
        events = service.get_accepted_events()

        # Serializăm lista.
        serializer = EventSerializer(
            events,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)
