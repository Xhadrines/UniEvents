from .base_repository import BaseRepository

from domain.models import Event


class EventRepository(BaseRepository):
    def __init__(self):
        super().__init__(Event)

    def get_upcoming_events(self):
        # Returneaza evenimentele care urmeaza
        from django.utils import timezone

        return self.model.objects.filter(start_date__gte=timezone.now()).order_by(
            "start_date"
        )

    def get_by_category(self, category_id: int):
        # Returneaza evenimente dupa categorie
        return self.model.objects.filter(category_id=category_id)

    def get_by_organizer(self, organizer_id: int):
        # Returneaza evenimente dupa organizator
        return self.model.objects.filter(organizer_id=organizer_id)

    def get_by_location(self, location_id: int):
        # Returneaza evenimente dupa locatie
        return self.model.objects.filter(location_id=location_id)

    def get_by_participation_type(self, participation_type_id: int):
        # Returneaza evenimente dupa tipul de participare
        return self.model.objects.filter(participation_type_id=participation_type_id)

    def get_accepted_events(self):
        return self.model.objects.filter(status__name__iexact="Acceptat")
