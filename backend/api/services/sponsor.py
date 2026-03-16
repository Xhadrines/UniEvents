from .base_service import BaseService

from ..repository import SponsorRepository


class SponsorService(BaseService):
    def __init__(self):
        super().__init__(SponsorRepository())
