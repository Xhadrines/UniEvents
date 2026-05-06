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
    def get(self, request, event_id):
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
            file=request.FILES.get("file"),
            is_public=request.data.get("is_public", True),
        )

        return Response(
            EventMaterialSerializer(material).data,
            status=status.HTTP_201_CREATED,
        )
