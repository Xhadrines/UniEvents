class BaseService:
    """
    Service de bază pentru operațiile comune ale aplicației.

    Acest service funcționează ca un strat intermediar
    între:
    - views/controllers
    - și repository-uri.

    Scopul lui este:
    - să centralizeze logica comună,
    - să evite duplicarea codului,
    - să ofere o structură mai curată aplicației.
    """

    def __init__(self, repository):
        """
        Primim repository-ul care va fi folosit de service.

        Exemplu:
        - UserService -> UserRepository
        - EventService -> EventRepository
        """

        self.repository = repository

    def get_all(self):
        """
        Returnează toate obiectele.
        """

        return self.repository.get_all()

    def get_by_id(self, obj_id):
        """
        Returnează un obiect după ID.
        """

        return self.repository.get_by_id(obj_id)

    def get_by_name(self, name):
        """
        Returnează un obiect după câmpul `name`.
        """

        return self.repository.get_by_name(name)

    def get_id_by_name(self, name):
        """
        Returnează ID-ul unui obiect după nume.
        """

        return self.repository.get_id_by_name(name)

    def create(self, **data):
        """
        Creează un obiect nou.

        Datele sunt trimise mai departe către repository.
        """

        return self.repository.create(**data)

    def update(self, obj_id, data):
        """
        Actualizează complet un obiect existent.
        """

        return self.repository.update(obj_id, **data)

    def partial_update(self, obj_id, data):
        """
        Actualizează parțial un obiect.

        Se modifică doar câmpurile primite.
        """

        return self.repository.partial_update(obj_id, **data)

    def delete(self, obj_id):
        """
        Șterge un obiect după ID.
        """

        return self.repository.delete(obj_id)
