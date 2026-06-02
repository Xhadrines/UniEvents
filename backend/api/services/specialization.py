from .base_service import BaseService

from ..repository import SpecializationRepository


class SpecializationService(BaseService):
    """
    Service responsabil pentru gestionarea specializărilor.

    Exemple:
    - Informatică,
    - Calculatoare,
    - Automatică,
    - Electronică.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu SpecializationRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Specialization.
        """

        super().__init__(SpecializationRepository())

    def get_by_faculty_id(self, faculty_id):
        """
        Returnează toate specializările
        asociate unei facultăți.

        faculty_id reprezintă ID-ul facultății
        pentru care vrem să obținem specializările.
        """

        return self.repository.get_by_faculty_id(faculty_id)
