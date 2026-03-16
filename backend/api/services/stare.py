from .base_service import BaseService

from ..repository import StareRepository


class StareService(BaseService):
    def __init__(self):
        super().__init__(StareRepository())
