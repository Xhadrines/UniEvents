from .base_repository import BaseRepository

from domain.models import Category


class CategoryRepository(BaseRepository):
    def __init__(self):
        super().__init__(Category)
