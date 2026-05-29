from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import FeedbackService, EventService
from domain.serializers import FeedbackSerializer


class FeedbackView(BaseCRUDView):
    service = FeedbackService()
    serializer_class = FeedbackSerializer


class AddFeedbackView(APIView):
    def post(self, request, event_id):
        feedback_service = FeedbackService()
        event_service = EventService()

        event = event_service.get_by_id(event_id)

        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        try:
            feedback = feedback_service.create_feedback(
                user=request.user,
                event=event,
                rating=request.data.get("rating"),
                comment=request.data.get("comment", ""),
            )

            return Response(
                FeedbackSerializer(feedback).data,
                status=status.HTTP_201_CREATED,
            )

        except ValueError as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )


class EventFeedbackListView(APIView):
    def get(self, request, event_id):
        feedback_service = FeedbackService()
        feedbacks = feedback_service.get_by_event(event_id).order_by("-created_at")

        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)
