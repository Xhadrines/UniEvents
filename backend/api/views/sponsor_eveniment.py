from .base_crud_view import BaseCRUDView

from ..services import SponsorEvenimentService
from ..serializers import SponsorEvenimentSerializer


class SponsorEvenimentView(BaseCRUDView):
    service = SponsorEvenimentService()
    serializer_class = SponsorEvenimentSerializer
