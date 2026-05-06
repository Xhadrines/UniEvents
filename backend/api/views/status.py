from .base_crud import BaseCRUDView

from ..services import StatusService
from ..serializers import StatusSerializer


class StatusView(BaseCRUDView):
    service = StatusService()
    serializer_class = StatusSerializer
