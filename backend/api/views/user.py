from .base_crud_view import BaseCRUDView

from ..services import UserService
from ..serializers import UserSerializer


class UserView(BaseCRUDView):
    service = UserService()
    serializer_class = UserSerializer
