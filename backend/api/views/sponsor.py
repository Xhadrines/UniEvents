from .base_crud_view import BaseCRUDView

from ..services import SponsorService
from ..serializers import SponsorSerializer


class SponsorView(BaseCRUDView):
    service = SponsorService()
    serializer_class = SponsorSerializer
