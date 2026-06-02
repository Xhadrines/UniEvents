from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import FeedbackService, EventService
from domain.serializers import FeedbackSerializer


class FeedbackView(BaseCRUDView):
    """
    View CRUD pentru feedback-uri.

    Moștenește BaseCRUDView,
    deci primește automat operațiile:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica feedback-urilor.
    service = FeedbackService()

    # Serializer-ul folosit pentru validare și serializare.
    serializer_class = FeedbackSerializer


class AddFeedbackView(APIView):
    """
    View responsabil pentru adăugarea unui feedback
    la un anumit eveniment.
    """

    def post(self, request, event_id):
        """
        Creează feedback pentru un eveniment.

        Reguli:
        - evenimentul trebuie să existe,
        - feedback-ul este permis doar după terminarea evenimentului,
        - utilizatorul poate adăuga un singur feedback per eveniment.
        """

        # Inițializăm service-urile necesare.
        feedback_service = FeedbackService()
        event_service = EventService()

        # Căutăm evenimentul după ID.
        event = event_service.get_by_id(event_id)

        # Dacă evenimentul nu există, returnăm 404.
        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            # Încercăm să creăm feedback-ul.
            feedback = feedback_service.create_feedback(
                user=request.user,
                event=event,
                rating=request.data.get("rating"),
                comment=request.data.get("comment", ""),
            )

            # Returnăm feedback-ul creat.
            return Response(
                FeedbackSerializer(feedback).data,
                status=status.HTTP_201_CREATED,
            )

        except ValueError as error:
            # Dacă service-ul aruncă o eroare de validare,
            # o trimitem către frontend cu status 400.
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class EventFeedbackListView(APIView):
    """
    View folosit pentru afișarea tuturor feedback-urilor
    unui eveniment.
    """

    def get(self, request, event_id):
        """
        Returnează feedback-urile unui eveniment,
        sortate de la cel mai nou la cel mai vechi.
        """

        # Inițializăm service-ul.
        feedback_service = FeedbackService()

        # Obținem feedback-urile evenimentului
        # și le sortăm descrescător după data creării.
        feedbacks = feedback_service.get_by_event(event_id).order_by("-created_at")

        # Serializăm lista de feedback-uri.
        serializer = FeedbackSerializer(feedbacks, many=True)

        return Response(serializer.data)
