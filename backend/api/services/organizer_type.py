from .base_service import BaseService

from ..repository import OrganizerTypeRepository


class OrganizerTypeService(BaseService):
    """
    Service responsabil pentru gestionarea tipurilor de organizatori.

    Exemple:
    - facultate,
    - companie,
    - organizație,
    - asociație studențească.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu OrganizerTypeRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul OrganizerType.
        """

        super().__init__(OrganizerTypeRepository())
