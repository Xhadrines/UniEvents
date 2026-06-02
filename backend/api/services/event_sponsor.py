from .base_service import BaseService

from ..repository import EventSponsorRepository


class EventSponsorService(BaseService):
    """
    Service responsabil pentru gestionarea relației
    dintre evenimente și sponsori.

    Acest service permite:
    - obținerea sponsorilor unui eveniment,
    - obținerea evenimentelor asociate unui sponsor.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu EventSponsorRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul EventSponsor.
        """

        super().__init__(EventSponsorRepository())

    def get_by_event(self, event_id: int):
        """
        Returnează sponsorii unui eveniment.

        event_id reprezintă ID-ul evenimentului
        pentru care vrem să obținem sponsorii.
        """

        return self.repository.get_by_event(event_id)

    def get_by_sponsor(self, sponsor_id: int):
        """
        Returnează toate evenimentele asociate unui sponsor.

        sponsor_id reprezintă ID-ul sponsorului
        pentru care vrem să obținem evenimentele sponsorizate.
        """

        return self.repository.get_by_sponsor(sponsor_id)
