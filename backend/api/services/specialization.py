from .base_service import BaseService

from ..repository import SpecializationRepository


class SpecializationService(BaseService):
    def __init__(self):
        super().__init__(SpecializationRepository())

    def get_by_faculty_id(self, faculty_id):
        return self.repository.get_by_faculty_id(faculty_id)
