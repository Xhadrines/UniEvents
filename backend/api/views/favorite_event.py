from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import FavoriteEventService, EventService
from ..serializers import FavoriteEventSerializer


class FavoriteEventView(BaseCRUDView):
    service = FavoriteEventService()
    serializer_class = FavoriteEventSerializer


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

        favorite = favorite_service.add_to_favorites(request.user, event)

        return Response(
            FavoriteEventSerializer(favorite).data,
            status=status.HTTP_201_CREATED,
        )


class RemoveFavoriteEventView(APIView):
    def delete(self, request, event_id):
        service = FavoriteEventService()
        deleted = service.remove_from_favorites(request.user.id, event_id)

        if not deleted:
            return Response(
                {"error": "Favorite event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
