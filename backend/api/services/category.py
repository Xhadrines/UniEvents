from .base_service import BaseService

from ..repository import CategoryRepository


class CategoryService(BaseService):
    """
    Service responsabil pentru logica legată de categorii.

    Acest service folosește CategoryRepository
    pentru accesul la baza de date.

    În acest moment moștenește doar operațiile comune
    din BaseService, dar aici poate fi adăugată ulterior
    logică specifică pentru categorii.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu CategoryRepository.

        Astfel, toate metodele din BaseService
        vor lucra pe modelul Category.
        """

        super().__init__(CategoryRepository())
