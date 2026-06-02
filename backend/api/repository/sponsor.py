from .base_repository import BaseRepository

from domain.models import Sponsor


class SponsorRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea sponsorilor.

    Sponsorii pot fi:
    - companii,
    - organizații,
    - parteneri ai evenimentelor.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Sponsor.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela Sponsor.
        """

        super().__init__(Sponsor)
