from .base_crud import BaseCRUDView

from ..services import ReportService
from domain.serializers import ReportSerializer


class ReportView(BaseCRUDView):
    service = ReportService()
    serializer_class = ReportSerializer
