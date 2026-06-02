from .base_crud import BaseCRUDView

from ..services import NotificationTypeService
from domain.serializers import NotificationTypeSerializer


class NotificationTypeView(BaseCRUDView):
    """
    View CRUD pentru tipurile de notificări.

    Exemple:
    - reminder,
    - confirmare înscriere,
    - anulare eveniment,
    - notificare sistem.
    """

    # Service-ul care gestionează logica
    # tipurilor de notificări.
    service = NotificationTypeService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = NotificationTypeSerializer
