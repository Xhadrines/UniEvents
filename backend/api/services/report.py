from .base_service import BaseService

from ..repository import ReportRepository


class ReportService(BaseService):
    def __init__(self):
        super().__init__(ReportRepository())

    def get_by_user(self, user_id: int):
        return self.repository.get_by_user(user_id)

    def create_report(self, generated_by, title: str, description: str = "", file=None):
        # Creeaza un raport generat de administrator
        return self.repository.create(
            generated_by=generated_by,
            title=title,
            description=description,
            file=file,
        )
