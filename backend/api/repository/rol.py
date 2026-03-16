from .base_repository import BaseRepository

from ..models import Rol


class RolRepository(BaseRepository):
    def __init__(self):
        super().__init__(Rol)
