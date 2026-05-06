from .base_repository import BaseRepository

from ..models import Role


class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__(Role)
