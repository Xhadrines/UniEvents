from .base_service import BaseService

from ..repository import SpecializareRepository


class SpecializareService(BaseService):
    def __init__(self):
        super().__init__(SpecializareRepository())
