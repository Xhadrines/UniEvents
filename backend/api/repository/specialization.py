from .base_repository import BaseRepository

from domain.models import Specialization


class SpecializationRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea specializărilor.

    Exemple:
    - Informatică,
    - Automatică,
    - Calculatoare,
    - Electronică.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Specialization.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela Specialization.
        """

        super().__init__(Specialization)

    def get_by_faculty_id(self, faculty_id):
        """
        Returnează toate specializările
        asociate unei facultăți.

        faculty_id reprezintă ID-ul facultății
        pentru care vrem să obținem specializările.
        """

        # Filtrăm specializările după facultate.
        return self.model.objects.filter(faculty_id=faculty_id)
