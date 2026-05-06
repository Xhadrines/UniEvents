from .base_crud import BaseCRUDView

from ..services import CategoryService
from ..serializers import CategorySerializer


class CategoryView(BaseCRUDView):
    service = CategoryService()
    serializer_class = CategorySerializer
