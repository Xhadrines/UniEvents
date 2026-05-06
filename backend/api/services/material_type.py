from .base_service import BaseService

from ..repository import MaterialTypeRepository


class MaterialTypeService(BaseService):
    def __init__(self):
        super().__init__(MaterialTypeRepository())
