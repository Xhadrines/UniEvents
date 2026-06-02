from .base_service import BaseService

from ..repository import EventMaterialRepository


class EventMaterialService(BaseService):
    """
    Service responsabil pentru gestionarea materialelor
    asociate evenimentelor.

    Exemple de materiale:
    - PDF-uri,
    - imagini,
    - prezentări,
    - documente,
    - resurse utile pentru participanți.
    """

    def __init__(self):
        """
        Inițializăm service-ul cu EventMaterialRepository.

        Toate metodele moștenite din BaseService
        vor opera pe modelul EventMaterial.
        """

        super().__init__(EventMaterialRepository())

    def get_by_event(self, event_id: int):
        """
        Returnează toate materialele asociate unui eveniment.
        """

        return self.repository.get_by_event(event_id)

    def upload_material(
        self, event, uploaded_by, material_type, title: str, file, is_public=True
    ):
        """
        Încarcă un material nou pentru un eveniment.

        Parametri:
        - event -> evenimentul asociat materialului
        - uploaded_by -> utilizatorul care încarcă materialul
        - material_type -> tipul materialului
        - title -> titlul materialului
        - file -> fișierul efectiv încărcat
        - is_public -> stabilește dacă materialul este public
        """

        # Creăm înregistrarea în baza de date
        # pentru materialul încărcat.
        return self.repository.create(
            event=event,
            uploaded_by=uploaded_by,
            material_type=material_type,
            title=title,
            file=file,
            is_public=is_public,
        )
