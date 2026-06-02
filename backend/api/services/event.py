from django.utils import timezone

from .base_service import BaseService
from ..repository import EventRepository


class EventService(BaseService):
    """
    Service responsabil pentru logica legată de evenimente.

    Acest service gestionează:
    - filtrarea evenimentelor,
    - validarea evenimentelor,
    - anularea evenimentelor,
    - obținerea evenimentelor acceptate sau viitoare.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu EventRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Event.
        """

        super().__init__(EventRepository())

    def get_upcoming_events(self):
        """
        Returnează evenimentele viitoare.

        Practic:
        - eliminăm evenimentele deja trecute,
        - păstrăm doar evenimentele care urmează.
        """

        return self.repository.get_upcoming_events()

    def get_by_category(self, category_id: int):
        """
        Returnează evenimentele filtrate după categorie.
        """

        return self.repository.get_by_category(category_id)

    def get_by_organizer(self, organizer_id: int):
        """
        Returnează evenimentele unui organizator.
        """

        return self.repository.get_by_organizer(organizer_id)

    def get_by_location(self, location_id: int):
        """
        Returnează evenimentele filtrate după locație.
        """

        return self.repository.get_by_location(location_id)

    def get_by_participation_type(self, participation_type_id: int):
        """
        Returnează evenimentele filtrate după tipul de participare.

        Exemple:
        - online,
        - fizic,
        - hibrid.
        """

        return self.repository.get_by_participation_type(participation_type_id)

    def validate_event(
        self,
        event_id: int,
        admin_user,
        accepted_status,
        max_files=None,
        max_file_size_mb=None,
    ):
        """
        Validează un eveniment.

        Această metodă este folosită de administrator
        pentru aprobarea unui eveniment.

        În timpul validării:
        - statusul devine "acceptat",
        - se salvează administratorul care a validat,
        - se salvează data validării,
        - se pot seta limite pentru fișiere.
        """

        # Căutăm evenimentul după ID.
        event = self.repository.get_by_id(event_id)

        # Dacă evenimentul nu există, returnăm None.
        if not event:
            return None

        # Dacă este trimisă limita maximă de fișiere,
        # actualizăm valoarea.
        if max_files is not None:
            event.max_files = max_files

        # Dacă este trimisă limita maximă de dimensiune,
        # actualizăm valoarea.
        if max_file_size_mb is not None:
            event.max_file_size_mb = max_file_size_mb

        # Actualizăm statusul evenimentului.
        event.status = accepted_status

        # Salvăm administratorul care a făcut validarea.
        event.validated_by = admin_user

        # Salvăm momentul validării.
        event.validated_at = timezone.now()

        # Salvăm toate modificările în baza de date.
        event.save()

        return event

    def cancel_event(self, event_id: int, cancelled_status):
        """
        Anulează un eveniment.

        Practic:
        - modificăm statusul evenimentului
          în statusul de anulare.
        """

        # Căutăm evenimentul după ID.
        event = self.repository.get_by_id(event_id)

        # Dacă evenimentul nu există, returnăm None.
        if not event:
            return None

        # Setăm statusul de anulare.
        event.status = cancelled_status

        # Salvăm modificările.
        event.save()

        return event

    def get_accepted_events(self):
        """
        Returnează doar evenimentele acceptate/aprobate.
        """

        return self.repository.get_accepted_events()
