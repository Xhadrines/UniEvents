from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .base_crud import BaseCRUDView
from ..services import EventMaterialService, EventService, MaterialTypeService
from domain.serializers import EventMaterialSerializer


class EventMaterialView(BaseCRUDView):
    service = EventMaterialService()
    serializer_class = EventMaterialSerializer


class EventMaterialsByEventView(APIView):
    def get(self, _request, event_id):
        service = EventMaterialService()
        materials = service.get_by_event(event_id)
        serializer = EventMaterialSerializer(materials, many=True)
        return Response(serializer.data)


class UploadEventMaterialView(APIView):
    def post(self, request, event_id):
        event_service = EventService()
        material_type_service = MaterialTypeService()
        material_service = EventMaterialService()

        event = event_service.get_by_id(event_id)

        if not event:
            return Response(
                {"error": "Event not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        file_obj = request.FILES.get("file")
        if not file_obj:
            return Response(
                {"error": "File is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if event.max_files is not None:
            current_files = material_service.get_by_event(event_id).count()
            if current_files >= event.max_files:
                return Response(
                    {"error": "Event file limit reached"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        if event.max_file_size_mb is not None:
            max_bytes = event.max_file_size_mb * 1024 * 1024
            if file_obj.size > max_bytes:
                return Response(
                    {
                        "error": (
                            f"File exceeds the allowed limit of {event.max_file_size_mb} MB"
                        )
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        material_type = material_type_service.get_by_id(
            request.data.get("material_type")
        )

        if not material_type:
            return Response(
                {"error": "Material type not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        material = material_service.upload_material(
            event=event,
            uploaded_by=request.user,
            material_type=material_type,
            title=request.data.get("title"),
            file=file_obj,
            is_public=str(request.data.get("is_public", "true")).lower()
            in ["true", "1", "yes", "da"],
        )

        return Response(
            EventMaterialSerializer(material).data,
            status=status.HTTP_201_CREATED,
        )
