from .base_crud import BaseCRUDView

from ..services import RoleService
from domain.serializers import RoleSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import EmailService


class RoleView(BaseCRUDView):
    """
    View CRUD pentru rolurile utilizatorilor.

    Exemple de roluri:
    - Student,
    - Profesor,
    - Administrator,
    - Organizator.
    """

    # Service-ul care gestionează logica rolurilor.
    service = RoleService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = RoleSerializer


class AdminRoleRequestView(APIView):
    """
    View responsabil pentru trimiterea unei cereri
    de rol administrator.

    Utilizatorul poate trimite un mesaj
    către administratorii aplicației.
    """

    def post(self, request):
        """
        Trimite cererea pentru rol de administrator.
        """

        # Obținem mesajul trimis de utilizator.
        #
        # strip():
        # elimină spațiile inutile de la început și sfârșit.
        message = request.data.get("message", "").strip()

        # Verificăm dacă mesajul există.
        if not message:
            return Response(
                {"error": "Mesajul este obligatoriu."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Inițializăm service-ul pentru email.
        email_service = EmailService()

        # Trimitem email-ul către administrator.
        email_service.send_admin_role_request_email(
            user=request.user,
            message=message,
        )

        # Returnăm mesaj de succes.
        return Response(
            {"message": ("Cererea a fost trimisă către administrator.")},
            status=status.HTTP_200_OK,
        )
