from .base_crud_view import BaseCRUDView

from ..services import CategorieService
from ..serializers import CategorieSerializer


class CategorieView(BaseCRUDView):
    service = CategorieService()
    serializer_class = CategorieSerializer
