from .base_crud import BaseCRUDView

from ..services import LocationService
from domain.serializers import LocationSerializer


class LocationView(BaseCRUDView):
    service = LocationService()
    serializer_class = LocationSerializer
