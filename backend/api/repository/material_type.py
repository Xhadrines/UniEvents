from .base_repository import BaseRepository

from domain.models import MaterialType


class MaterialTypeRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea tipurilor de materiale.

    Exemple de tipuri:
    - PDF,
    - imagine,
    - video,
    - prezentare,
    - document.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul MaterialType.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela MaterialType.
        """

        super().__init__(MaterialType)
