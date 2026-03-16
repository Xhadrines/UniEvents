from .base_crud_view import BaseCRUDView

from ..services import StareService
from ..serializers import StareSerializer


class StareView(BaseCRUDView):
    service = StareService()
    serializer_class = StareSerializer
