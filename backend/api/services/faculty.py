from .base_service import BaseService

from ..repository import FacultyRepository


class FacultyService(BaseService):
    """
    Service responsabil pentru logica legată de facultăți.

    Acest service folosește FacultyRepository
    pentru accesul la baza de date.

    În acest moment moștenește operațiile comune
    din BaseService, dar aici poate fi adăugată ulterior
    logică specifică facultăților.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu FacultyRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Faculty.
        """

        super().__init__(FacultyRepository())
