from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import (
    FavoriteEventService,
    EventService,
    NotificationTypeService,
    NotificationService,
    EmailService,
)
from domain.serializers import FavoriteEventSerializer


class FavoriteEventView(BaseCRUDView):
    service = FavoriteEventService()
    serializer_class = FavoriteEventSerializer


class MyFavoriteEventsView(APIView):
    def get(self, request):
        service = FavoriteEventService()
        favorites = service.get_by_user(request.user.id)
        serializer = FavoriteEventSerializer(
            favorites,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)


class AddFavoriteEventView(APIView):
    def post(self, request, event_id):
        event_service = EventService()
        favorite_service = FavoriteEventService()

        event = event_service.get_by_id(event_id)

        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        already_favorite = favorite_service.repository.get_by_user_and_event(
            request.user.id,
            event.id,
        )

        favorite = favorite_service.add_to_favorites(request.user, event)

        if not already_favorite:
            notification_type_service = NotificationTypeService()
            notification_service = NotificationService()
            email_service = EmailService()

            notification_type = notification_type_service.get_by_name("reminder")

            if not notification_type:
                notification_type = notification_type_service.create(
                    name="reminder",
                    description="Reminder pentru evenimente favorite",
                )

            notification_service.create_notification(
                user=request.user,
                title="Eveniment adăugat la favorite",
                message=f'Ai adăugat "{event.name}" la favorite. Îți vom reaminti înainte de eveniment.',
                notification_type=notification_type,
                event=event,
            )

            email_service.send_favorite_event_email(
                user=request.user,
                event=event,
            )

        return Response(
            FavoriteEventSerializer(favorite).data,
            status=status.HTTP_201_CREATED,
        )


class RemoveFavoriteEventView(APIView):
    def delete(self, request, event_id):
        favorite_service = FavoriteEventService()
        event_service = EventService()
        notification_type_service = NotificationTypeService()
        notification_service = NotificationService()
        email_service = EmailService()

        event = event_service.get_by_id(event_id)

        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        deleted = favorite_service.remove_from_favorites(
            request.user.id,
            event_id,
        )

        if not deleted:
            return Response(
                {"error": "Favorite event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        notification_type = notification_type_service.get_by_name("reminder")

        if not notification_type:
            notification_type = notification_type_service.create(
                name="reminder",
                description="Reminder pentru evenimente favorite",
            )

        notification_service.create_notification(
            user=request.user,
            title="Eveniment eliminat de la favorite",
            message=f'Ai eliminat "{event.name}" din lista ta de favorite.',
            notification_type=notification_type,
            event=event,
        )

        email_service.send_favorite_event_removed_email(
            user=request.user,
            event=event,
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
