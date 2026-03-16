from .base_crud_view import BaseCRUDView

from ..services import OrganizatorService
from ..serializers import OrganizatorSerializer


class OrganizatorView(BaseCRUDView):
    service = OrganizatorService()
    serializer_class = OrganizatorSerializer
