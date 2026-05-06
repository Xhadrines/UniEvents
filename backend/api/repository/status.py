from .base_repository import BaseRepository

from domain.models import Status


class StatusRepository(BaseRepository):
    def __init__(self):
        super().__init__(Status)
