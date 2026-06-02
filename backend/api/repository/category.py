from .base_repository import BaseRepository

from domain.models import Category


class CategoryRepository(BaseRepository):
    """
    Repository responsabil pentru operațiile legate de modelul Category.

    Acest repository moștenește toate metodele CRUD
    din BaseRepository:
    - create()
    - get_all()
    - get_by_id()
    - update()
    - delete()
    etc.

    Astfel evităm să rescriem aceeași logică pentru fiecare model.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul Category.

        Practic spunem:
        "toate operațiile din BaseRepository
        vor lucra pe tabela Category".
        """

        super().__init__(Category)
