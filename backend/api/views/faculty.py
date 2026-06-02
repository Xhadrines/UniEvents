from .base_crud import BaseCRUDView

from ..services import FacultyService
from domain.serializers import FacultySerializer


class FacultyView(BaseCRUDView):
    """
    View CRUD pentru facultăți.

    Moștenește BaseCRUDView,
    deci oferă automat operațiile:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica facultăților.
    service = FacultyService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = FacultySerializer
