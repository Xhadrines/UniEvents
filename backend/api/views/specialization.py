from .base_crud import BaseCRUDView

from ..services import SpecializationService
from domain.serializers import SpecializationSerializer


class SpecializationView(BaseCRUDView):
    service = SpecializationService()
    serializer_class = SpecializationSerializer
