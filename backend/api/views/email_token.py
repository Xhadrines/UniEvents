from .base_crud import BaseCRUDView

from ..services import EmailTokenService
from domain.serializers import EmailTokenSerializer


class EmailTokenView(BaseCRUDView):
    """
    View responsabil pentru operațiile CRUD
    asupra token-urilor de email.

    Token-urile sunt folosite pentru:
    - completarea profilului,
    - confirmarea contului,
    - validarea unor acțiuni sensibile.
    """

    # Service-ul care gestionează logica
    # pentru token-urile de email.
    service = EmailTokenService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializarea obiectelor,
    # - transformarea datelor JSON.
    serializer_class = EmailTokenSerializer
