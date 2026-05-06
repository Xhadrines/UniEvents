from .base_crud import BaseCRUDView

from ..services import EventSponsorService
from ..serializers import EventSponsorSerializer


class EventSponsorView(BaseCRUDView):
    service = EventSponsorService()
    serializer_class = EventSponsorSerializer
