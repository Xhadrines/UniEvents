from .base_crud_view import BaseCRUDView

from ..services import UserProfilesService
from ..serializers import UserProfilesSerializer


class UserProfilesView(BaseCRUDView):
    service = UserProfilesService()
    serializer_class = UserProfilesSerializer
