from .base_crud_view import BaseCRUDView

from ..services import LocatieService
from ..serializers import LocatieSerializer


class LocatieView(BaseCRUDView):
    service = LocatieService()
    serializer_class = LocatieSerializer
