from typing import Any, Optional, Type

from django.db import models
from django.db.models import QuerySet


class BaseRepository:
    """
    Repository de bază folosit pentru operațiile CRUD comune.

    CRUD = Create, Read, Update, Delete

    Ideea acestui repository este să evităm duplicarea codului
    în toate repository-urile aplicației.
    """

    def __init__(self, model: Type[models.Model]):
        # Salvăm modelul Django primit ca parametru.
        # Exemplu:
        # UserRepository -> primește modelul User
        # EventRepository -> primește modelul Event
        self.model = model

    def get_all(self) -> QuerySet:
        """
        Returnează toate înregistrările din tabel.
        """
        return self.model.objects.all()

    def get_by_id(self, obj_id: int) -> Optional[models.Model]:
        """
        Caută un obiect după ID.

        Folosim filter(...).first() în loc de get()
        pentru a evita excepțiile dacă obiectul nu există.
        """
        return self.model.objects.filter(id=obj_id).first()

    def create(self, **data: Any) -> models.Model:
        """
        Creează un obiect nou în baza de date.

        **data înseamnă că putem trimite câmpuri dinamice:
        exemplu:
        create(name="Alex", email="alex@gmail.com")
        """
        return self.model.objects.create(**data)

    def update(self, obj_id: int, **data: Any) -> Optional[models.Model]:
        """
        Actualizează complet un obiect existent.

        Parcurgem toate câmpurile modelului și actualizăm
        doar valorile primite în request.
        """

        # Căutăm obiectul după ID.
        obj = self.get_by_id(obj_id)

        # Dacă obiectul nu există, returnăm None.
        if not obj:
            return None

        # Parcurgem toate câmpurile modelului.
        for field in obj._meta.fields:
            field_name = field.name

            # Verificăm dacă acel câmp există în datele primite.
            if field_name in data:
                # Setăm noua valoare pe obiect.
                setattr(obj, field_name, data[field_name])

        # Salvăm modificările în baza de date.
        obj.save()

        return obj

    def partial_update(self, obj_id: int, **data: Any) -> Optional[models.Model]:
        """
        Actualizare parțială a unui obiect.

        Diferența față de update():
        aici actualizăm doar câmpurile trimise,
        fără să ne intereseze toate câmpurile modelului.
        """

        # Căutăm obiectul după ID.
        obj = self.get_by_id(obj_id)

        # Dacă obiectul nu există, oprim execuția.
        if not obj:
            return None

        # Parcurgem toate datele primite.
        for key, value in data.items():

            # Verificăm dacă obiectul are acel atribut.
            # Evităm erori dacă se trimite un câmp invalid.
            if hasattr(obj, key):
                setattr(obj, key, value)

        # Salvăm modificările.
        obj.save()

        return obj

    def delete(self, obj_id: int) -> bool:
        """
        Șterge un obiect după ID.

        Returnează:
        - True  -> dacă ștergerea a reușit
        - False -> dacă obiectul nu există
        """

        # Căutăm obiectul.
        obj = self.get_by_id(obj_id)

        # Dacă nu există, returnăm False.
        if not obj:
            return False

        # Ștergem obiectul din baza de date.
        obj.delete()

        return True

    def get_by_field(self, field_name: str, value: Any) -> Optional[models.Model]:
        """
        Caută un singur obiect după orice câmp primit dinamic.

        Exemplu:
        get_by_field("email", "alex@gmail.com")
        """

        return self.model.objects.filter(**{field_name: value}).first()

    def get_all_by_field(self, field_name: str, value: Any) -> QuerySet:
        """
        Returnează toate obiectele care respectă condiția dată.

        Exemplu:
        get_all_by_field("status", "ACTIVE")
        """

        return self.model.objects.filter(**{field_name: value})

    def get_by_name(self, name: str) -> Optional[models.Model]:
        """
        Metodă ajutătoare pentru modelele care au câmpul `name`.
        """

        return self.get_by_field("name", name)

    def get_all_by_name(self, name: str) -> QuerySet:
        """
        Returnează toate obiectele care au același nume.
        """

        return self.get_all_by_field("name", name)

    def get_id_by_name(self, name: str) -> Optional[int]:
        """
        Returnează doar ID-ul unui obiect după nume.

        Folosim only("id") pentru optimizare:
        Django va aduce din baza de date doar coloana `id`,
        nu întregul obiect.
        """

        obj = self.model.objects.filter(name=name).only("id").first()

        return obj.id if obj else None

    def get_instance_by_name(self, name: str) -> Optional[models.Model]:
        """
        Alias pentru get_by_name().

        A fost păstrat pentru compatibilitate cu datele default
        sau cod mai vechi din aplicație.
        """

        return self.get_by_name(name)

    def set_password(self, user, password: str):
        """
        Setează parola unui utilizator în mod securizat.

        IMPORTANT:
        Nu salvăm niciodată parola ca text simplu.

        set_password():
        - face hash la parolă
        - aplică algoritmul securizat Django
        - pregătește parola pentru autentificare
        """

        user.set_password(password)

        # Salvăm utilizatorul cu noua parolă hash-uită.
        user.save()

        return user
