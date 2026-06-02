from .base_service import BaseService

from ..repository import OrganizerRepository


class OrganizerService(BaseService):
    """
    Service responsabil pentru gestionarea organizatorilor.

    Organizatorii pot reprezenta:
    - facultăți,
    - companii,
    - organizații,
    - utilizatori care creează evenimente.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu OrganizerRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Organizer.
        """

        super().__init__(OrganizerRepository())

    def get_by_user(self, user_id: int):
        """
        Returnează organizatorul asociat unui utilizator.

        Folosim user_id pentru a găsi relația
        dintre utilizator și organizator.
        """

        # Căutăm organizatorul după câmpul user_id.
        return self.repository.get_by_field("user_id", user_id)
