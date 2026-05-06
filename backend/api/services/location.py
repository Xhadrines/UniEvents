from .base_service import BaseService

from ..repository import LocationRepository


class LocationService(BaseService):
    def __init__(self):
        super().__init__(LocationRepository())
