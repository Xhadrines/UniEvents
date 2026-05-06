from .base_crud import BaseCRUDView

from ..services import EventSponsorService
from domain.serializers import EventSponsorSerializer


class EventSponsorView(BaseCRUDView):
    service = EventSponsorService()
    serializer_class = EventSponsorSerializer
