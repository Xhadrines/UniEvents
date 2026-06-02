from .base_service import BaseService

from ..repository import RoleRepository


class RoleService(BaseService):
    """
    Service responsabil pentru gestionarea rolurilor utilizatorilor.

    Acest service este folosit pentru:
    - obținerea rolurilor,
    - atribuirea automată a rolului
      pe baza adresei de email.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu RoleRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul Role.
        """

        super().__init__(RoleRepository())

    def assign_role_from_email(self, email: str):
        """
        Alege automat rolul utilizatorului
        pe baza domeniului email-ului.

        Reguli:
        - @student.usv.ro -> Student
        - @usv.ro -> Profesor
        - orice alt domeniu -> Altele
        """

        # Extragem partea de după '@'.
        #
        # Exemplu:
        # alex@student.usv.ro -> student.usv.ro
        domain = email.split("@")[-1].lower()

        # Stabilim rolul în funcție de domeniu.
        if domain == "student.usv.ro":
            role_name = "Student"

        elif domain == "usv.ro":
            role_name = "Profesor"

        else:
            role_name = "Altele"

        # Returnăm obiectul Role corespunzător.
        return self.get_by_name(role_name)
