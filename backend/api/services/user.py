from .base_service import BaseService

from ..repository import UserRepository


class UserService(BaseService):
    def __init__(self):
        super().__init__(UserRepository())
