from .base_repository import BaseRepository

from ..models import Status


class StatusRepository(BaseRepository):
    def __init__(self):
        super().__init__(Status)
