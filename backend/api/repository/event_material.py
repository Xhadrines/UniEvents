from .base_repository import BaseRepository

from domain.models import EventMaterial


class EventMaterialRepository(BaseRepository):
    """
    Repository responsabil pentru operațiile legate de materialele
    asociate unui eveniment.

    Exemple de materiale:
    - PDF-uri,
    - prezentări,
    - imagini,
    - documentație,
    - link-uri utile.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul EventMaterial.

        Astfel, toate metodele moștenite din BaseRepository
        vor lucra pe tabela EventMaterial.
        """

        super().__init__(EventMaterial)

    def get_by_event(self, event_id: int):
        """
        Returnează toate materialele asociate unui eveniment.

        event_id reprezintă ID-ul evenimentului pentru care
        vrem să obținem materialele.
        """

        # Filtrăm toate materialele care aparțin evenimentului.
        return self.model.objects.filter(event_id=event_id)
