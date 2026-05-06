from .base_service import BaseService

from ..repository import CategoryRepository


class CategoryService(BaseService):
    def __init__(self):
        super().__init__(CategoryRepository())
