from .base_service import BaseService

from ..repository import RolRepository


class RolService(BaseService):
    def __init__(self):
        super().__init__(RolRepository())
