from .base_crud_view import BaseCRUDView

from ..services import FacultateService
from ..serializers import FacultateSerializer


class FacultateView(BaseCRUDView):
    service = FacultateService()
    serializer_class = FacultateSerializer
