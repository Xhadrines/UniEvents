from .base_crud import BaseCRUDView

from ..services import RoleService
from domain.serializers import RoleSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import EmailService


class RoleView(BaseCRUDView):
    service = RoleService()
    serializer_class = RoleSerializer


class AdminRoleRequestView(APIView):
    def post(self, request):
        message = request.data.get("message", "").strip()

        if not message:
            return Response(
                {"error": "Mesajul este obligatoriu."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        email_service = EmailService()
        email_service.send_admin_role_request_email(
            user=request.user,
            message=message,
        )

        return Response(
            {"message": "Cererea a fost trimisă către administrator."},
            status=status.HTTP_200_OK,
        )
