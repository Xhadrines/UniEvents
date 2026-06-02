from .base_repository import BaseRepository

from domain.models import Report


class ReportRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea rapoartelor.

    Rapoartele pot fi folosite pentru:
    - statistici,
    - exporturi,
    - analize,
    - documente generate automat de sistem.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Report.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela Report.
        """

        super().__init__(Report)

    def get_by_user(self, user_id: int):
        """
        Returnează toate rapoartele generate de un utilizator.

        generated_by_id reprezintă utilizatorul
        care a generat raportul.
        """

        return self.model.objects.filter(generated_by_id=user_id)
