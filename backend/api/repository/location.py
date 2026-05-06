from .base_repository import BaseRepository

from domain.models import Location


class LocationRepository(BaseRepository):
    def __init__(self):
        super().__init__(Location)
