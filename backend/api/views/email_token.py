from .base_crud import BaseCRUDView

from ..services import EmailTokenService
from ..serializers import EmailTokenSerializer


class EmailTokenView(BaseCRUDView):
    service = EmailTokenService()
    serializer_class = EmailTokenSerializer
