from .base_crud import BaseCRUDView

from ..services import LocationService
from domain.serializers import LocationSerializer


class LocationView(BaseCRUDView):
    """
    View CRUD pentru locații.

    Moștenește BaseCRUDView,
    deci oferă automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica locațiilor.
    service = LocationService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = LocationSerializer
