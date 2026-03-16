from .base_service import BaseService

from ..repository import CategorieRepository


class CategorieService(BaseService):
    def __init__(self):
        super().__init__(CategorieRepository())
