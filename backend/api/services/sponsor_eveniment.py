from .base_service import BaseService

from ..repository import SponsorEvenimentRepository


class SponsorEvenimentService(BaseService):
    def __init__(self):
        super().__init__(SponsorEvenimentRepository())
