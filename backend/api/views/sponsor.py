from .base_crud import BaseCRUDView

from ..services import SponsorService
from domain.serializers import SponsorSerializer


class SponsorView(BaseCRUDView):
    service = SponsorService()
    serializer_class = SponsorSerializer
