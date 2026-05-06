from .base_repository import BaseRepository

from domain.models import MaterialType


class MaterialTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(MaterialType)
