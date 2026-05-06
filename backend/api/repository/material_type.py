from .base_repository import BaseRepository

from ..models import MaterialType


class MaterialTypeRepository(BaseRepository):
    def __init__(self):
        super().__init__(MaterialType)
