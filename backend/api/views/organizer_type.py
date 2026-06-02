from .base_crud import BaseCRUDView

from ..services import OrganizerTypeService
from domain.serializers import OrganizerTypeSerializer


class OrganizerTypeView(BaseCRUDView):
    """
    View CRUD pentru tipurile de organizatori.

    Exemple:
    - facultate,
    - companie,
    - organizație,
    - asociație studențească.
    """

    # Service-ul care gestionează logica
    # tipurilor de organizatori.
    service = OrganizerTypeService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = OrganizerTypeSerializer
