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
