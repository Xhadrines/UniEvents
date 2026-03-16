from .base_service import BaseService

from ..repository import OrganizatorRepository


class OrganizatorService(BaseService):
    def __init__(self):
        super().__init__(OrganizatorRepository())
