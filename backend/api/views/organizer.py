from .base_crud import BaseCRUDView

from ..services import OrganizerService
from domain.serializers import OrganizerSerializer


class OrganizerView(BaseCRUDView):
    """
    View CRUD pentru organizatori.

    Organizatorii pot reprezenta:
    - utilizatori,
    - facultăți,
    - companii,
    - organizații,
    - asociații studențești.
    """

    # Service-ul care gestionează logica organizatorilor.
    service = OrganizerService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = OrganizerSerializer
