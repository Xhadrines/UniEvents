class BaseService:

    def __init__(self, repository):
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, obj_id):
        return self.repository.get_by_id(obj_id)

    def get_by_name(self, name):
        return self.repository.get_by_name(name)

    def get_id_by_name(self, name):
        return self.repository.get_id_by_name(name)

    def create(self, **data):
        return self.repository.create(**data)

    def update(self, obj_id, data):
        return self.repository.update(obj_id, **data)

    def partial_update(self, obj_id, data):
        return self.repository.partial_update(obj_id, **data)

    def delete(self, obj_id):
        return self.repository.delete(obj_id)
