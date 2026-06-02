from .base_repository import BaseRepository

from domain.models import Event


class EventRepository(BaseRepository):
    """
    Repository responsabil pentru operațiile legate de evenimente.

    Acest repository conține metode specifice pentru:
    - filtrarea evenimentelor,
    - căutarea după categorie/locație/organizator,
    - obținerea evenimentelor viitoare,
    - obținerea evenimentelor acceptate.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Event.

        Toate metodele moștenite din BaseRepository
        vor lucra automat pe tabela Event.
        """

        super().__init__(Event)

    def get_upcoming_events(self):
        """
        Returnează toate evenimentele care urmează să aibă loc.

        start_date__gte înseamnă:
        "start_date mai mare sau egal cu momentul curent".

        Practic:
        - eliminăm evenimentele deja trecute,
        - păstrăm doar evenimentele viitoare.
        """

        # timezone.now() returnează data și ora curentă.
        from django.utils import timezone

        # Sortăm rezultatele crescător după data de început,
        # astfel încât primul eveniment să fie cel mai apropiat.
        return self.model.objects.filter(start_date__gte=timezone.now()).order_by(
            "start_date"
        )

    def get_by_category(self, category_id: int):
        """
        Returnează toate evenimentele dintr-o anumită categorie.

        Exemplu:
        - Workshop
        - Conferință
        - Hackathon
        """

        return self.model.objects.filter(category_id=category_id)

    def get_by_organizer(self, organizer_id: int):
        """
        Returnează toate evenimentele create de un organizator.
        """

        return self.model.objects.filter(organizer_id=organizer_id)

    def get_by_location(self, location_id: int):
        """
        Returnează toate evenimentele dintr-o anumită locație.
        """

        return self.model.objects.filter(location_id=location_id)

    def get_by_participation_type(self, participation_type_id: int):
        """
        Returnează evenimentele filtrate după tipul de participare.

        Exemple:
        - fizic,
        - online,
        - hibrid.
        """

        return self.model.objects.filter(participation_type_id=participation_type_id)

    def get_accepted_events(self):
        """
        Returnează doar evenimentele aprobate/acceptate.

        status__name__iexact:
        - verifică valoarea câmpului status.name
        - ignoră diferențele dintre litere mari și mici
          (Acceptat == acceptat == ACCEPTAT)
        """

        return self.model.objects.filter(status__name__iexact="Acceptat")
