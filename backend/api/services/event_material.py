from .base_service import BaseService

from ..repository import EventMaterialRepository


class EventMaterialService(BaseService):
    def __init__(self):
        super().__init__(EventMaterialRepository())

    def get_by_event(self, event_id: int):
        return self.repository.get_by_event(event_id)

    def upload_material(
        self, event, uploaded_by, material_type, title: str, file, is_public=True
    ):
        # Incarca un material pentru un eveniment
        return self.repository.create(
            event=event,
            uploaded_by=uploaded_by,
            material_type=material_type,
            title=title,
            file=file,
            is_public=is_public,
        )
