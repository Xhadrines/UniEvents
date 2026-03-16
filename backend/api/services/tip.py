from .base_service import BaseService

from ..repository import TipRepository


class TipService(BaseService):
    def __init__(self):
        super().__init__(TipRepository())
