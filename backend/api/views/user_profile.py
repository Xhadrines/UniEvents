from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import UserProfileService, EmailTokenService
from domain.serializers import UserProfileSerializer


class UserProfileView(BaseCRUDView):
    service = UserProfileService()
    serializer_class = UserProfileSerializer


class CompleteProfileView(APIView):
    def get(self, request):
        service = UserProfileService()
        data = service.get_faculties_and_specializations()
        return Response(data)

    def post(self, request):
        token_str = request.query_params.get("token") or request.data.get("token")

        if not token_str:
            return Response(
                {"error": "Token missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        email_token_service = EmailTokenService()
        token_obj = email_token_service.validate_token(token_str)

        if not token_obj:
            return Response(
                {"error": "Invalid or used token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        profile_service = UserProfileService()
        profile_data = profile_service.complete_profile(
            token_obj.user,
            request.data,
        )

        email_token_service.mark_as_used(token_obj)

        return Response(profile_data, status=status.HTTP_200_OK)


class MyProfileUpdateView(APIView):
    def patch(self, request):
        service = UserProfileService()

        try:
            result = service.update_my_profile(
                user=request.user,
                data=request.data,
            )

            user = result["user"]
            profile = result["profile"]

            return Response(
                {
                    "user_id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "date_joined": user.date_joined,
                    "profile": UserProfileSerializer(profile).data,
                },
                status=status.HTTP_200_OK,
            )

        except ValueError as error:
            return Response(
                {"error": str(error)},
                status=status.HTTP_400_BAD_REQUEST,
            )
