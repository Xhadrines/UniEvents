from .base_service import BaseService

from ..repository import TipParticipareRepository


class TipParticipareService(BaseService):
    def __init__(self):
        super().__init__(TipParticipareRepository())
