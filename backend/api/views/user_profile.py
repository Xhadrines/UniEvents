from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import UserProfileService, EmailTokenService
from domain.serializers import UserProfileSerializer


class UserProfileView(BaseCRUDView):
    """
    View CRUD pentru profilele utilizatorilor.

    Moștenește BaseCRUDView,
    deci oferă automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica profilelor.
    service = UserProfileService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = UserProfileSerializer


class CompleteProfileView(APIView):
    """
    View responsabil pentru completarea profilului utilizatorului.

    Este folosit mai ales:
    - după autentificarea Google,
    - după înregistrare,
    - când utilizatorul trebuie să completeze date suplimentare.
    """

    def get(self, request):
        """
        Returnează datele necesare formularului de profil.

        Exemplu:
        - facultăți,
        - specializări.
        """

        # Inițializăm service-ul profilului.
        service = UserProfileService()

        # Obținem datele necesare formularului.
        data = service.get_faculties_and_specializations()

        return Response(data)

    def post(self, request):
        """
        Completează profilul utilizatorului
        folosind token-ul primit prin email.
        """

        # Obținem token-ul:
        # - fie din query params,
        # - fie din request body.
        token_str = request.query_params.get("token") or request.data.get("token")

        # Dacă token-ul lipsește.
        if not token_str:
            return Response(
                {"error": "Token missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Inițializăm service-ul token-urilor.
        email_token_service = EmailTokenService()

        # Validăm token-ul.
        token_obj = email_token_service.validate_token(token_str)

        # Dacă token-ul este invalid sau deja folosit.
        if not token_obj:
            return Response(
                {"error": "Invalid or used token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Inițializăm service-ul profilului.
        profile_service = UserProfileService()

        # Completăm profilul utilizatorului.
        profile_data = profile_service.complete_profile(
            token_obj.user,
            request.data,
        )

        # Marcăm token-ul ca folosit,
        # pentru a preveni reutilizarea.
        email_token_service.mark_as_used(token_obj)

        # Returnăm profilul completat.
        return Response(profile_data, status=status.HTTP_200_OK)


class MyProfileUpdateView(APIView):
    """
    View responsabil pentru actualizarea profilului
    utilizatorului autentificat.
    """

    def patch(self, request):
        """
        Actualizează:
        - datele utilizatorului,
        - datele profilului.
        """

        # Inițializăm service-ul profilului.
        service = UserProfileService()

        try:
            # Actualizăm profilul.
            result = service.update_my_profile(
                user=request.user,
                data=request.data,
            )

            # Extragem utilizatorul actualizat.
            user = result["user"]

            # Extragem profilul actualizat.
            profile = result["profile"]

            # Returnăm datele actualizate.
            return Response(
                {
                    "user_id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "date_joined": user.date_joined,
                    # Serializăm profilul.
                    "profile": UserProfileSerializer(profile).data,
                },
                status=status.HTTP_200_OK,
            )

        except ValueError as error:
            # Dacă apare eroare de validare,
            # returnăm mesajul către frontend.
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )
