from .base_crud import BaseCRUDView

from ..services import StatusService
from domain.serializers import StatusSerializer


class StatusView(BaseCRUDView):
    """
    View CRUD pentru statusuri.

    Statusurile sunt folosite în aplicație pentru:
    - evenimente,
    - înscrieri,
    - utilizatori,
    - notificări,
    - alte entități care au stări diferite.
    """

    # Service-ul care gestionează logica statusurilor.
    service = StatusService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = StatusSerializer
