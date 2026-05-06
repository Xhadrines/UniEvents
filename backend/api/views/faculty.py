from .base_crud import BaseCRUDView

from ..services import FacultyService
from ..serializers import FacultySerializer


class FacultyView(BaseCRUDView):
    service = FacultyService()
    serializer_class = FacultySerializer
