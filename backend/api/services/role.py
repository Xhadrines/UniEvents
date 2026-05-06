from .base_service import BaseService

from ..repository import RoleRepository


class RoleService(BaseService):
    def __init__(self):
        super().__init__(RoleRepository())

    def assign_role_from_email(self, email: str):
        # Alege rolul utilizatorului pe baza domeniului emailului
        domain = email.split("@")[-1].lower()

        if domain == "student.usv.ro":
            role_name = "Student"
        elif domain == "usv.ro":
            role_name = "Profesor"
        else:
            role_name = "Altele"

        return self.get_by_name(role_name)
