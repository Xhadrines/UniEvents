from .base_service import BaseService

from ..repository import MaterialTypeRepository


class MaterialTypeService(BaseService):
    """
    Service responsabil pentru gestionarea tipurilor de materiale.

    Exemple de tipuri:
    - PDF,
    - imagine,
    - video,
    - document,
    - prezentare.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu MaterialTypeRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul MaterialType.
        """

        super().__init__(MaterialTypeRepository())
