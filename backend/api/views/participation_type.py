from .base_crud import BaseCRUDView

from ..services import ParticipationTypeService
from ..serializers import ParticipationTypeSerializer


class ParticipationTypeView(BaseCRUDView):
    service = ParticipationTypeService()
    serializer_class = ParticipationTypeSerializer
