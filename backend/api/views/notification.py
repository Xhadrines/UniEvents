from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import NotificationService
from domain.serializers import NotificationSerializer


class NotificationView(BaseCRUDView):
    service = NotificationService()
    serializer_class = NotificationSerializer


class MyNotificationsView(APIView):
    def get(self, request):
        service = NotificationService()
        notifications = service.get_by_user(request.user.id)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)


class UnreadNotificationsView(APIView):
    def get(self, request):
        service = NotificationService()
        notifications = service.get_unread_by_user(request.user.id)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)


class MarkNotificationAsReadView(APIView):
    def post(self, request, notification_id):
        service = NotificationService()
        notification = service.mark_as_read(notification_id)

        if not notification:
            return Response(
                {"error": "Notification not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(NotificationSerializer(notification).data)
