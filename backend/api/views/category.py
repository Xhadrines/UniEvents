from .base_crud import BaseCRUDView

from ..services import CategoryService
from domain.serializers import CategorySerializer


class CategoryView(BaseCRUDView):
    """
    View responsabil pentru operațiile CRUD
    asupra categoriilor.

    Această clasă moștenește BaseCRUDView,
    deci primește automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care conține logica aplicației
    # pentru categorii.
    service = CategoryService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - transformarea obiectelor în JSON,
    # - transformarea JSON -> obiecte Django.
    serializer_class = CategorySerializer
