from .base_crud import BaseCRUDView

from ..services import NotificationTypeService
from ..serializers import NotificationTypeSerializer


class NotificationTypeView(BaseCRUDView):
    service = NotificationTypeService()
    serializer_class = NotificationTypeSerializer
