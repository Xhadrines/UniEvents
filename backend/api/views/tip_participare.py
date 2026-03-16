from .base_crud_view import BaseCRUDView

from ..services import TipParticipareService
from ..serializers import TipParticipareSerializer


class TipParticipareView(BaseCRUDView):
    service = TipParticipareService()
    serializer_class = TipParticipareSerializer
