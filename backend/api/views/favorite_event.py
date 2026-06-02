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
    """
    View CRUD pentru evenimentele favorite.

    Moștenește BaseCRUDView,
    deci oferă automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica favorite-urilor.
    service = FavoriteEventService()

    # Serializer-ul folosit pentru:
    # - validare,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = FavoriteEventSerializer


class MyFavoriteEventsView(APIView):
    """
    View folosit pentru obținerea
    evenimentelor favorite ale utilizatorului autentificat.
    """

    def get(self, request):
        """
        Returnează lista evenimentelor favorite
        ale utilizatorului curent.
        """

        # Inițializăm service-ul.
        service = FavoriteEventService()

        # Obținem favoritele utilizatorului.
        favorites = service.get_by_user(request.user.id)

        # Serializăm lista.
        serializer = FavoriteEventSerializer(
            favorites,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


class AddFavoriteEventView(APIView):
    """
    View responsabil pentru adăugarea
    unui eveniment la favorite.
    """

    def post(self, request, event_id):
        """
        Adaugă un eveniment la favorite.

        Dacă evenimentul este adăugat pentru prima dată:
        - se creează notificare,
        - se trimite email utilizatorului.
        """

        event_service = EventService()
        favorite_service = FavoriteEventService()

        # Căutăm evenimentul.
        event = event_service.get_by_id(event_id)

        # Dacă evenimentul nu există.
        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Verificăm dacă evenimentul există deja la favorite.
        already_favorite = favorite_service.repository.get_by_user_and_event(
            request.user.id,
            event.id,
        )

        # Adăugăm evenimentul la favorite.
        favorite = favorite_service.add_to_favorites(request.user, event)

        # Dacă evenimentul a fost adăugat acum pentru prima dată.
        if not already_favorite:

            notification_type_service = NotificationTypeService()
            notification_service = NotificationService()
            email_service = EmailService()

            # Obținem tipul notificării "reminder".
            notification_type = notification_type_service.get_by_name("reminder")

            # Dacă tipul notificării nu există,
            # îl creăm automat.
            if not notification_type:
                notification_type = notification_type_service.create(
                    name="reminder",
                    description="Reminder pentru evenimente favorite",
                )

            # Creăm notificarea pentru utilizator.
            notification_service.create_notification(
                user=request.user,
                title="Eveniment adăugat la favorite",
                message=(
                    f'Ai adăugat "{event.name}" la favorite. '
                    f"Îți vom reaminti înainte de eveniment."
                ),
                notification_type=notification_type,
                event=event,
            )

            # Trimitem email utilizatorului.
            email_service.send_favorite_event_email(
                user=request.user,
                event=event,
            )

        # Returnăm obiectul creat.
        return Response(
            FavoriteEventSerializer(favorite).data,
            status=status.HTTP_201_CREATED,
        )


class RemoveFavoriteEventView(APIView):
    """
    View responsabil pentru eliminarea
    unui eveniment din favorite.
    """

    def delete(self, request, event_id):
        """
        Elimină evenimentul din lista de favorite.

        După eliminare:
        - se creează notificare,
        - se trimite email utilizatorului.
        """

        favorite_service = FavoriteEventService()
        event_service = EventService()
        notification_type_service = NotificationTypeService()
        notification_service = NotificationService()
        email_service = EmailService()

        # Căutăm evenimentul.
        event = event_service.get_by_id(event_id)

        # Dacă evenimentul nu există.
        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Eliminăm evenimentul din favorite.
        deleted = favorite_service.remove_from_favorites(
            request.user.id,
            event_id,
        )

        # Dacă evenimentul nu era la favorite.
        if not deleted:
            return Response(
                {"error": "Favorite event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Obținem tipul notificării.
        notification_type = notification_type_service.get_by_name("reminder")

        # Dacă tipul notificării nu există,
        # îl creăm automat.
        if not notification_type:
            notification_type = notification_type_service.create(
                name="reminder",
                description="Reminder pentru evenimente favorite",
            )

        # Creăm notificarea pentru utilizator.
        notification_service.create_notification(
            user=request.user,
            title="Eveniment eliminat de la favorite",
            message=(f'Ai eliminat "{event.name}" ' f"din lista ta de favorite."),
            notification_type=notification_type,
            event=event,
        )

        # Trimitem email utilizatorului.
        email_service.send_favorite_event_removed_email(
            user=request.user,
            event=event,
        )

        # 204 = ștergere reușită fără conținut returnat.
        return Response(status=status.HTTP_204_NO_CONTENT)
