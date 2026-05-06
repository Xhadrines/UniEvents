from .base_service import BaseService

from ..repository import OrganizerTypeRepository


class OrganizerTypeService(BaseService):
    def __init__(self):
        super().__init__(OrganizerTypeRepository())
