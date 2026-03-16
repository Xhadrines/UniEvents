from .base_service import BaseService

from ..repository import FacultateRepository


class FacultateService(BaseService):
    def __init__(self):
        super().__init__(FacultateRepository())
