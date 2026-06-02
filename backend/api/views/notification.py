from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import NotificationService
from domain.serializers import NotificationSerializer


class NotificationView(BaseCRUDView):
    """
    View CRUD pentru notificări.

    Moștenește BaseCRUDView,
    deci oferă automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica notificărilor.
    service = NotificationService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = NotificationSerializer


class MyNotificationsView(APIView):
    """
    View folosit pentru obținerea tuturor notificărilor
    utilizatorului autentificat.
    """

    def get(self, request):
        """
        Returnează notificările utilizatorului curent.
        """

        # Inițializăm service-ul notificărilor.
        service = NotificationService()

        # Obținem notificările utilizatorului.
        notifications = service.get_by_user(request.user.id)

        # Serializăm lista notificărilor.
        serializer = NotificationSerializer(notifications, many=True)

        return Response(serializer.data)


class UnreadNotificationsView(APIView):
    """
    View folosit pentru obținerea notificărilor necitite.
    """

    def get(self, request):
        """
        Returnează doar notificările necitite
        ale utilizatorului autentificat.
        """

        # Inițializăm service-ul notificărilor.
        service = NotificationService()

        # Obținem notificările necitite.
        notifications = service.get_unread_by_user(request.user.id)

        # Serializăm lista notificărilor.
        serializer = NotificationSerializer(notifications, many=True)

        return Response(serializer.data)


class MarkNotificationAsReadView(APIView):
    """
    View responsabil pentru marcarea unei notificări
    ca fiind citită.
    """

    def post(self, request, notification_id):
        """
        Marchează notificarea ca citită.
        """

        # Inițializăm service-ul.
        service = NotificationService()

        # Marcăm notificarea ca citită.
        notification = service.mark_as_read(notification_id)

        # Dacă notificarea nu există -> 404.
        if not notification:
            return Response(
                {"error": "Notification not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Returnăm notificarea actualizată.
        return Response(NotificationSerializer(notification).data)
