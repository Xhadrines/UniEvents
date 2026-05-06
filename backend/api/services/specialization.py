from .base_service import BaseService

from ..repository import SpecializationRepository


class SpecializationService(BaseService):
    def __init__(self):
        super().__init__(SpecializationRepository())
