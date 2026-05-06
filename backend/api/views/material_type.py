from .base_crud import BaseCRUDView

from ..services import MaterialTypeService
from ..serializers import MaterialTypeSerializer


class MaterialTypeView(BaseCRUDView):
    service = MaterialTypeService()
    serializer_class = MaterialTypeSerializer
