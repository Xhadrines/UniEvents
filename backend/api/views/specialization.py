from rest_framework.response import Response

from .base_crud import BaseCRUDView

from ..services import SpecializationService
from domain.serializers import SpecializationSerializer


class SpecializationView(BaseCRUDView):
    service = SpecializationService()
    serializer_class = SpecializationSerializer

    def get(self, request, pk=None):
        if pk:
            return super().get(request, pk)

        faculty_id = request.query_params.get("faculty")

        if faculty_id:
            specializations = self.service.get_by_faculty_id(faculty_id)
        else:
            specializations = self.service.get_all()

        serializer = self.serializer_class(specializations, many=True)
        return Response(serializer.data)
