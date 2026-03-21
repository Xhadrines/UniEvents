from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import GoogleAuthService


class GoogleAuthView(APIView):
    def post(self, request):
        token = request.data.get("token")

        if not token:
            return Response(
                {"error": "Token missing"}, status=status.HTTP_400_BAD_REQUEST
            )

        service = GoogleAuthService()
        result = service.authenticate(token)

        if not result:
            return Response(
                {"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST
            )

        return Response(result, status=status.HTTP_200_OK)
