from .base_crud_view import BaseCRUDView

from ..services import RolService
from ..serializers import RolSerializer


class RolView(BaseCRUDView):
    service = RolService()
    serializer_class = RolSerializer
