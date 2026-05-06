from .base_repository import BaseRepository

from domain.models import Role


class RoleRepository(BaseRepository):
    def __init__(self):
        super().__init__(Role)
