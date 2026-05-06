from typing import Any, Optional, Type

from django.db import models
from django.db.models import QuerySet


class BaseRepository:
    # Repository de baza pentru operatii CRUD comune

    def __init__(self, model: Type[models.Model]):
        self.model = model

    def get_all(self) -> QuerySet:
        return self.model.objects.all()

    def get_by_id(self, obj_id: int) -> Optional[models.Model]:
        return self.model.objects.filter(id=obj_id).first()

    def create(self, **data: Any) -> models.Model:
        return self.model.objects.create(**data)

    def update(self, obj_id: int, **data: Any) -> Optional[models.Model]:
        obj = self.get_by_id(obj_id)

        if not obj:
            return None

        for field in obj._meta.fields:
            field_name = field.name

            if field_name in data:
                setattr(obj, field_name, data[field_name])

        obj.save()
        return obj

    def partial_update(self, obj_id: int, **data: Any) -> Optional[models.Model]:
        obj = self.get_by_id(obj_id)

        if not obj:
            return None

        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        obj.save()
        return obj

    def delete(self, obj_id: int) -> bool:
        obj = self.get_by_id(obj_id)

        if not obj:
            return False

        obj.delete()
        return True

    def get_by_field(self, field_name: str, value: Any) -> Optional[models.Model]:
        # Cauta un obiect dupa orice camp primit ca parametru
        return self.model.objects.filter(**{field_name: value}).first()

    def get_all_by_field(self, field_name: str, value: Any) -> QuerySet:
        # Cauta toate obiectele dupa orice camp primit ca parametru
        return self.model.objects.filter(**{field_name: value})

    def get_by_name(self, name: str) -> Optional[models.Model]:
        # Pentru modelele care au campul name
        return self.get_by_field("name", name)

    def get_all_by_name(self, name: str) -> QuerySet:
        # Pentru modelele care au campul name
        return self.get_all_by_field("name", name)

    def get_id_by_name(self, name: str) -> Optional[int]:
        # Returneaza id-ul dupa campul name
        obj = self.model.objects.filter(name=name).only("id").first()
        return obj.id if obj else None

    def get_instance_by_name(self, name: str) -> Optional[models.Model]:
        # Alias pastrat pentru compatibilitate cu datele default
        return self.get_by_name(name)
