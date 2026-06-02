from .base_crud import BaseCRUDView

from ..services import ParticipationTypeService
from domain.serializers import ParticipationTypeSerializer


class ParticipationTypeView(BaseCRUDView):
    """
    View CRUD pentru tipurile de participare.

    Exemple:
    - online,
    - fizic,
    - hibrid.
    """

    # Service-ul care gestionează logica
    # tipurilor de participare.
    service = ParticipationTypeService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = ParticipationTypeSerializer
