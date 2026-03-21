from .base_service import BaseService

from ..repository import RolRepository


class RolService(BaseService):
    def __init__(self):
        super().__init__(RolRepository())

    def assign_role_from_email(self, email: str):
        domain = email.split("@")[-1].lower()

        if domain == "student.usv.ro":
            rol_nume = "Student"
        elif domain == "usm.ro":
            rol_nume = "Profesor"
        else:
            rol_nume = "Altele"

        return self.get_by_name(rol_nume)
