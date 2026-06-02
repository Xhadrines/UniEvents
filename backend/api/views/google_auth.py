from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..services import GoogleAuthService


class GoogleAuthView(APIView):
    """
    View responsabil pentru autentificarea utilizatorilor
    folosind Google OAuth.

    Flow:
    1. Frontend-ul trimite token-ul Google.
    2. Backend-ul validează token-ul la Google.
    3. Se verifică email-ul instituțional.
    4. Utilizatorul este autentificat sau creat automat.
    """

    def post(self, request):
        """
        Autentifică utilizatorul folosind token-ul Google.
        """

        # Obținem token-ul trimis de frontend.
        token = request.data.get("token")

        # Dacă token-ul lipsește,
        # returnăm eroare.
        if not token:
            return Response(
                {"error": "Token missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Inițializăm service-ul pentru autentificare Google.
        service = GoogleAuthService()

        # Încercăm autentificarea.
        result = service.authenticate(token)

        # Dacă autentificarea a eșuat:
        # - token invalid,
        # - token expirat,
        # - email neacceptat.
        if not result:
            return Response(
                {"error": "Invalid token or invalid student email"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Returnăm datele utilizatorului autentificat.
        #
        # De obicei:
        # - access token JWT,
        # - refresh token,
        # - date profil utilizator.
        return Response(result, status=status.HTTP_200_OK)
