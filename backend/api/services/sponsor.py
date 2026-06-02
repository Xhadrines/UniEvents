from .base_service import BaseService

from ..repository import SponsorRepository


class SponsorService(BaseService):
    """
    Service responsabil pentru gestionarea sponsorilor.

    Sponsorii pot fi:
    - companii,
    - organizații,
    - parteneri ai evenimentelor.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu SponsorRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Sponsor.
        """

        super().__init__(SponsorRepository())
