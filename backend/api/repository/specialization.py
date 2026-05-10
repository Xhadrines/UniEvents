from .base_repository import BaseRepository

from domain.models import Specialization


class SpecializationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Specialization)

    def get_by_faculty_id(self, faculty_id):
        return self.model.objects.filter(faculty_id=faculty_id)
