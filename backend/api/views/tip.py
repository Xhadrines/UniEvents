from .base_crud_view import BaseCRUDView

from ..services import TipService
from ..serializers import TipSerializer


class TipView(BaseCRUDView):
    service = TipService()
    serializer_class = TipSerializer
