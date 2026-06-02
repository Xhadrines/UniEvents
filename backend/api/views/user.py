from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .base_crud import BaseCRUDView
from ..services import UserService
from domain.serializers import UserSerializer


class UserView(BaseCRUDView):
    """
    View CRUD pentru utilizatori.

    Moștenește BaseCRUDView,
    deci oferă automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica utilizatorilor.
    service = UserService()

    # Serializer-ul folosit pentru validare și serializare.
    serializer_class = UserSerializer


class RegisterView(APIView):
    """
    View responsabil pentru înregistrarea utilizatorilor.
    """

    def post(self, request):
        """
        Creează un utilizator nou.

        Date necesare:
        - username
        - email
        - password
        """

        user_service = UserService()

        try:
            # Încercăm să înregistrăm utilizatorul.
            user = user_service.register(
                username=request.data.get("username"),
                email=request.data.get("email"),
                password=request.data.get("password"),
            )

            # Returnăm ID-ul utilizatorului creat.
            return Response(
                {"user_id": user.id},
                status=status.HTTP_201_CREATED,
            )

        except ValueError as error:
            # Dacă apare o eroare de validare,
            # o trimitem către frontend.
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        """
        Mesaj informativ pentru accesarea endpoint-ului prin GET.
        """

        return Response(
            {"message": "Register endpoint - send POST request"},
            status=status.HTTP_200_OK,
        )


class LoginView(APIView):
    """
    View responsabil pentru autentificarea utilizatorilor.
    """

    def post(self, request):
        """
        Autentifică utilizatorul cu username/email și parolă.

        Dacă login-ul reușește:
        - returnăm datele utilizatorului,
        - generăm access token,
        - generăm refresh token.
        """

        user_service = UserService()

        try:
            # Verificăm datele de login.
            data = user_service.login(
                username_or_email=request.data.get("username_or_email"),
                password=request.data.get("password"),
            )

            # Obținem obiectul User pentru generarea token-urilor JWT.
            user = user_service.get_by_id(data["user_id"])

            # Generăm refresh token.
            refresh = RefreshToken.for_user(user)

            # Adăugăm token-urile în răspuns.
            data["refresh"] = str(refresh)
            data["access"] = str(refresh.access_token)

            return Response(data, status=status.HTTP_200_OK)

        except ValueError as error:
            # Dacă autentificarea eșuează,
            # returnăm eroare.
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        """
        Mesaj informativ pentru accesarea endpoint-ului prin GET.
        """

        return Response(
            {"message": "Login endpoint - send POST request"},
            status=status.HTTP_200_OK,
        )


class PasswordResetRequestView(APIView):
    """
    View responsabil pentru cererea de resetare a parolei.
    """

    def post(self, request):
        """
        Trimite email pentru resetarea parolei.

        Din motive de securitate,
        răspunsul este același chiar dacă email-ul nu există.
        """

        user_service = UserService()

        try:
            # Pornim procesul de resetare a parolei.
            user_service.request_password_reset(
                email=request.data.get("email"),
            )

            return Response(
                {
                    "message": (
                        "Dacă email-ul există, " "vei primi un link de resetare."
                    )
                },
                status=status.HTTP_200_OK,
            )

        except ValueError as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        """
        Mesaj informativ pentru endpoint-ul de resetare parolă.
        """

        return Response(
            {"message": "Password reset endpoint - send POST request"},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(APIView):
    """
    View responsabil pentru confirmarea resetării parolei.
    """

    def post(self, request):
        """
        Setează parola nouă folosind:
        - uid
        - token
        - password
        """

        user_service = UserService()

        try:
            # Confirmăm resetarea parolei.
            user_service.confirm_password_reset(
                uid=request.data.get("uid"),
                token=request.data.get("token"),
                password=request.data.get("password"),
            )

            return Response(
                {"message": "Parola a fost resetată cu succes."},
                status=status.HTTP_200_OK,
            )

        except ValueError as error:
            # Dacă link-ul/token-ul este invalid
            # sau datele lipsesc, returnăm eroare.
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        """
        Mesaj informativ pentru endpoint-ul de confirmare resetare.
        """

        return Response(
            {"message": "Password reset confirm endpoint - send POST request"},
            status=status.HTTP_200_OK,
        )
