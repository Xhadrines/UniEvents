from .base_service import BaseService

from ..repository import StatusRepository


class StatusService(BaseService):
    """
    Service responsabil pentru gestionarea statusurilor.

    Exemple de statusuri:
    - Activ,
    - Acceptat,
    - Respins,
    - Anulat,
    - În așteptare.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu StatusRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Status.
        """

        super().__init__(StatusRepository())
