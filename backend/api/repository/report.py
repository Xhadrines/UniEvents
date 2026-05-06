from .base_repository import BaseRepository

from ..models import Report


class ReportRepository(BaseRepository):
    def __init__(self):
        super().__init__(Report)

    def get_by_user(self, user_id: int):
        # Returneaza rapoartele generate de un utilizator
        return self.model.objects.filter(generated_by_id=user_id)
