from .base_crud import BaseCRUDView

from ..services import EventSponsorService
from domain.serializers import EventSponsorSerializer


class EventSponsorView(BaseCRUDView):
    """
    View CRUD pentru relația dintre evenimente și sponsori.

    Această relație permite asocierea:
    - unui sponsor la un eveniment,
    - sau mai multor sponsori la același eveniment.
    """

    # Service-ul care gestionează logica
    # relației event-sponsor.
    service = EventSponsorService()

    # Serializer-ul folosit pentru:
    # - validare,
    # - serializare,
    # - transformarea datelor JSON.
    serializer_class = EventSponsorSerializer
