from .base_service import BaseService

from ..repository import ParticipationTypeRepository


class ParticipationTypeService(BaseService):
    """
    Service responsabil pentru gestionarea tipurilor de participare.

    Exemple:
    - online,
    - fizic,
    - hibrid.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu ParticipationTypeRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul ParticipationType.
        """

        super().__init__(ParticipationTypeRepository())
