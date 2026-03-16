from .base_service import BaseService

from ..repository import InregistrareRepository


class InregistrareService(BaseService):
    def __init__(self):
        super().__init__(InregistrareRepository())
