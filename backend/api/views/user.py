from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import UserService
from domain.serializers import UserSerializer


class UserView(BaseCRUDView):
    service = UserService()
    serializer_class = UserSerializer


class RegisterView(APIView):
    def post(self, request):
        user_service = UserService()

        try:
            user = user_service.register(
                username=request.data.get("username"),
                email=request.data.get("email"),
                password=request.data.get("password"),
            )

            return Response(
                {"user_id": user.id},
                status=status.HTTP_201_CREATED,
            )

        except ValueError as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        return Response(
            {"message": "Register endpoint - send POST request"},
            status=status.HTTP_200_OK,
        )


class LoginView(APIView):
    def post(self, request):
        user_service = UserService()

        try:
            data = user_service.login(
                username_or_email=request.data.get("username_or_email"),
                password=request.data.get("password"),
            )

            return Response(data, status=status.HTTP_200_OK)

        except ValueError as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        return Response(
            {"message": "Login endpoint - send POST request"},
            status=status.HTTP_200_OK,
        )


class PasswordResetRequestView(APIView):
    def post(self, request):
        user_service = UserService()

        try:
            user_service.request_password_reset(
                email=request.data.get("email"),
            )

            return Response(
                {"message": "Dacă email-ul există, vei primi un link de resetare."},
                status=status.HTTP_200_OK,
            )

        except ValueError as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        return Response(
            {"message": "Password reset endpoint - send POST request"},
            status=status.HTTP_200_OK,
        )


class PasswordResetConfirmView(APIView):
    def post(self, request):
        user_service = UserService()

        try:
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
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def get(self, request):
        return Response(
            {"message": "Password reset confirm endpoint - send POST request"},
            status=status.HTTP_200_OK,
        )
