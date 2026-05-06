from .base_service import BaseService

from ..repository import NotificationTypeRepository


class NotificationTypeService(BaseService):
    def __init__(self):
        super().__init__(NotificationTypeRepository())
