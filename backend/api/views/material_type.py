from .base_crud import BaseCRUDView

from ..services import MaterialTypeService
from domain.serializers import MaterialTypeSerializer


class MaterialTypeView(BaseCRUDView):
    """
    View CRUD pentru tipurile de materiale.

    Exemple de tipuri:
    - PDF,
    - imagine,
    - video,
    - document,
    - prezentare.
    """

    # Service-ul care gestionează logica
    # tipurilor de materiale.
    service = MaterialTypeService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = MaterialTypeSerializer
