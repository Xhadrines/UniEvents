from .base_crud import BaseCRUDView

from ..services import RoleService
from ..serializers import RoleSerializer


class RoleView(BaseCRUDView):
    service = RoleService()
    serializer_class = RoleSerializer
