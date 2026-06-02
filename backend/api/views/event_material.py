from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import (
    EventMaterialService,
    EventService,
    MaterialTypeService,
)
from domain.serializers import EventMaterialSerializer


class EventMaterialView(BaseCRUDView):
    """
    View CRUD pentru materialele evenimentelor.

    Moștenește BaseCRUDView,
    deci oferă automat:
    - GET
    - POST
    - PUT
    - PATCH
    - DELETE
    """

    # Service-ul care gestionează logica materialelor.
    service = EventMaterialService()

    # Serializer-ul folosit pentru validare și serializare.
    serializer_class = EventMaterialSerializer


class EventMaterialsByEventView(APIView):
    """
    View folosit pentru obținerea tuturor materialelor
    asociate unui eveniment.
    """

    def get(self, _request, event_id):
        """
        Returnează toate materialele
        asociate evenimentului primit.
        """

        # Inițializăm service-ul materialelor.
        service = EventMaterialService()

        # Obținem materialele evenimentului.
        materials = service.get_by_event(event_id)

        # Serializăm lista de materiale.
        serializer = EventMaterialSerializer(materials, many=True)

        return Response(serializer.data)


class UploadEventMaterialView(APIView):
    """
    View responsabil pentru încărcarea fișierelor
    asociate unui eveniment.
    """

    def post(self, request, event_id):
        """
        Încarcă un material nou pentru eveniment.

        Validări importante:
        - evenimentul trebuie să existe,
        - fișierul trebuie trimis,
        - numărul maxim de fișiere,
        - dimensiunea maximă permisă,
        - tipul materialului trebuie să existe.
        """

        # Inițializăm service-urile necesare.
        event_service = EventService()
        material_type_service = MaterialTypeService()
        material_service = EventMaterialService()

        # Căutăm evenimentul.
        event = event_service.get_by_id(event_id)

        # Dacă evenimentul nu există -> 404.
        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Obținem fișierul trimis în request.
        file_obj = request.FILES.get("file")

        # Dacă nu există fișier -> eroare.
        if not file_obj:
            return Response(
                {"error": "File is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Verificăm limita maximă de fișiere.
        if event.max_files is not None:

            # Numărăm fișierele deja încărcate.
            current_files = material_service.get_by_event(event_id).count()

            # Dacă s-a depășit limita.
            if current_files >= event.max_files:
                return Response(
                    {"error": "Event file limit reached"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Verificăm limita maximă de dimensiune.
        if event.max_file_size_mb is not None:

            # Convertim MB în bytes.
            max_bytes = event.max_file_size_mb * 1024 * 1024

            # Verificăm dimensiunea fișierului.
            if file_obj.size > max_bytes:
                return Response(
                    {
                        "error": (
                            f"File exceeds the allowed limit "
                            f"of {event.max_file_size_mb} MB"
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        # Obținem tipul materialului.
        material_type = material_type_service.get_by_id(
            request.data.get("material_type")
        )

        # Dacă tipul materialului nu există.
        if not material_type:
            return Response(
                {"error": "Material type not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Creăm materialul nou.
        material = material_service.upload_material(
            event=event,
            # Utilizatorul autentificat care încarcă fișierul.
            uploaded_by=request.user,
            material_type=material_type,
            # Titlul materialului.
            title=request.data.get("title"),
            # Fișierul efectiv.
            file=file_obj,
            # Convertim valorile text în boolean.
            #
            # Exemple acceptate:
            # true / 1 / yes / da
            is_public=str(request.data.get("is_public", "true")).lower()
            in ["true", "1", "yes", "da"],
        )

        # Returnăm materialul creat.
        return Response(
            EventMaterialSerializer(material).data,
            status=status.HTTP_201_CREATED,
        )
