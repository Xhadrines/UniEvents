from .base_crud import BaseCRUDView

from ..services import SponsorService
from domain.serializers import SponsorSerializer


class SponsorView(BaseCRUDView):
    """
    View CRUD pentru sponsori.

    Sponsorii pot reprezenta:
    - companii,
    - organizații,
    - parteneri,
    - instituții care susțin evenimentele.
    """

    # Service-ul care gestionează logica sponsorilor.
    service = SponsorService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = SponsorSerializer
