from rest_framework.response import Response

from .base_crud import BaseCRUDView

from ..services import SpecializationService
from domain.serializers import SpecializationSerializer


class SpecializationView(BaseCRUDView):
    """
    View CRUD pentru specializări.

    În plus față de operațiile CRUD standard,
    această clasă permite filtrarea specializărilor
    după facultate.
    """

    # Service-ul care gestionează logica specializărilor.
    service = SpecializationService()

    # Serializer-ul folosit pentru:
    # - validarea datelor,
    # - serializare,
    # - transformarea obiectelor în JSON.
    serializer_class = SpecializationSerializer

    def get(self, request, pk=None):
        """
        GET personalizat pentru specializări.

        Posibile situații:
        - dacă există pk -> returnăm o singură specializare
        - dacă există ?faculty=ID -> filtrăm după facultate
        - altfel -> returnăm toate specializările
        """

        # Dacă există pk,
        # folosim logica standard din BaseCRUDView.
        if pk:
            return super().get(request, pk)

        # Obținem parametrul faculty din query params.
        #
        # Exemplu:
        # /api/specializations/?faculty=1
        faculty_id = request.query_params.get("faculty")

        # Dacă există faculty_id,
        # filtrăm specializările după facultate.
        if faculty_id:

            specializations = self.service.get_by_faculty_id(faculty_id)

        else:
            # Dacă nu există filtru,
            # returnăm toate specializările.
            specializations = self.service.get_all()

        # Serializăm lista specializărilor.
        serializer = self.serializer_class(specializations, many=True)

        return Response(serializer.data)
