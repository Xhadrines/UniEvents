from .base_service import BaseService

from ..repository import LocationRepository


class LocationService(BaseService):
    """
    Service responsabil pentru logica legată de locații.

    Acest service folosește LocationRepository
    pentru accesul la datele din baza de date.

    În acest moment moștenește operațiile comune
    din BaseService, dar aici poate fi adăugată ulterior
    logică specifică locațiilor.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu LocationRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Location.
        """

        super().__init__(LocationRepository())
