from .base_crud_view import BaseCRUDView

from ..services import EvenimentService
from ..serializers import EvenimentSerializer


class EvenimentView(BaseCRUDView):
    service = EvenimentService()
    serializer_class = EvenimentSerializer
