from .base_repository import BaseRepository

from domain.models import EventSponsor


class EventSponsorRepository(BaseRepository):
    """
    Repository responsabil pentru relația dintre
    evenimente și sponsori.

    Acest model este folosit pentru a gestiona:
    - sponsorii unui eveniment,
    - evenimentele sponsorizate de un sponsor.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul EventSponsor.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela EventSponsor.
        """

        super().__init__(EventSponsor)

    def get_by_event(self, event_id: int):
        """
        Returnează toți sponsorii asociați unui eveniment.

        event_id = ID-ul evenimentului pentru care
        vrem să obținem sponsorii.
        """

        # Filtrăm toate relațiile care aparțin evenimentului.
        return self.model.objects.filter(event_id=event_id)

    def get_by_sponsor(self, sponsor_id: int):
        """
        Returnează toate evenimentele asociate unui sponsor.

        sponsor_id = ID-ul sponsorului pentru care
        vrem să obținem evenimentele sponsorizate.
        """

        # Filtrăm toate relațiile care aparțin sponsorului.
        return self.model.objects.filter(sponsor_id=sponsor_id)
