from .base_crud_view import BaseCRUDView

from ..services import InregistrareService
from ..serializers import InregistrareSerializer


class InregistrareView(BaseCRUDView):
    service = InregistrareService()
    serializer_class = InregistrareSerializer
