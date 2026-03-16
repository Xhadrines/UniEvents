from .base_crud_view import BaseCRUDView

from ..services import SpecializareService
from ..serializers import SpecializareSerializer


class SpecializareView(BaseCRUDView):
    service = SpecializareService()
    serializer_class = SpecializareSerializer
