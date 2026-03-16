from django.db import models
from typing import Type


class BaseRepository:

    def __init__(self, model: Type[models.Model]):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, obj_id):
        return self.model.objects.filter(id=obj_id).first()

    def create(self, **data):
        return self.model.objects.create(**data)

    def update(self, obj_id, **data):
        obj = self.get_by_id(obj_id)
        if not obj:
            return None

        for field in obj._meta.fields:
            name = field.name
            if name in data:
                setattr(obj, name, data[name])

        obj.save()
        return obj

    def partial_update(self, obj_id, **data):
        obj = self.get_by_id(obj_id)
        if not obj:
            return None

        for key, value in data.items():
            setattr(obj, key, value)

        obj.save()
        return obj

    def delete(self, obj_id):
        obj = self.get_by_id(obj_id)
        if not obj:
            return False

        obj.delete()
        return True
