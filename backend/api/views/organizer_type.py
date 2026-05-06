from .base_crud import BaseCRUDView

from ..services import OrganizerTypeService
from ..serializers import OrganizerTypeSerializer


class OrganizerTypeView(BaseCRUDView):
    service = OrganizerTypeService()
    serializer_class = OrganizerTypeSerializer
