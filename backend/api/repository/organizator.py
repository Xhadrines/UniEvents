from .base_repository import BaseRepository

from ..models import Organizator


class OrganizatorRepository(BaseRepository):
    def __init__(self):
        super().__init__(Organizator)
