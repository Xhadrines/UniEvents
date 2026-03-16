from .base_service import BaseService

from ..repository import LocatieRepository


class LocatieService(BaseService):
    def __init__(self):
        super().__init__(LocatieRepository())
