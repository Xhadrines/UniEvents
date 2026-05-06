from .base_crud import BaseCRUDView

from ..services import OrganizerService
from ..serializers import OrganizerSerializer


class OrganizerView(BaseCRUDView):
    service = OrganizerService()
    serializer_class = OrganizerSerializer
