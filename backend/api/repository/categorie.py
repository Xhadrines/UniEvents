from .base_repository import BaseRepository

from ..models import Categorie


class CategorieRepository(BaseRepository):
    def __init__(self):
        super().__init__(Categorie)
