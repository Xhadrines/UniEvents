from .base_service import BaseService

from ..repository import EvenimentRepository


class EvenimentService(BaseService):
    def __init__(self):
        super().__init__(EvenimentRepository())
