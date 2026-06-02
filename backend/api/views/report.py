from .base_crud import BaseCRUDView

from ..services import ReportService
from domain.serializers import ReportSerializer


class ReportView(BaseCRUDView):
    """
    View CRUD pentru rapoarte.

    Rapoartele pot conține:
    - statistici,
    - exporturi,
    - documente generate,
    - fișiere administrative.
    """

    # Service-ul care gestionează logica rapoartelor.
    service = ReportService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = ReportSerializer
