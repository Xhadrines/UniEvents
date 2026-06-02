from .base_service import BaseService

from ..repository import ReportRepository


class ReportService(BaseService):
    """
    Service responsabil pentru gestionarea rapoartelor.

    Acest service permite:
    - obținerea rapoartelor unui utilizator,
    - crearea rapoartelor generate de administratori,
    - salvarea fișierelor asociate rapoartelor.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu ReportRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Report.
        """

        super().__init__(ReportRepository())

    def get_by_user(self, user_id: int):
        """
        Returnează toate rapoartele generate
        de un utilizator.
        """

        return self.repository.get_by_user(user_id)

    def create_report(self, generated_by, title: str, description: str = "", file=None):
        """
        Creează un raport nou.

        Parametri:
        - generated_by -> utilizatorul care generează raportul
        - title -> titlul raportului
        - description -> descriere opțională
        - file -> fișier asociat raportului (opțional)
        """

        # Creăm raportul în baza de date.
        return self.repository.create(
            generated_by=generated_by,
            title=title,
            description=description,
            file=file,
        )
