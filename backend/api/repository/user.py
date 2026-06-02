from django.contrib.auth.models import User
from django.db.models import Q

from .base_repository import BaseRepository


class UserRepository(BaseRepository):
    """
    Repository responsabil pentru gestionarea utilizatorilor.

    Acest repository conține logica specifică:
    - autentificării,
    - căutării utilizatorilor,
    - creării conturilor,
    - actualizării profilului,
    - autentificării cu Google.
    """

    def __init__(self):
        """
        Inițializăm repository-ul cu modelul User din Django.

        Toate metodele moștenite din BaseRepository
        vor opera pe tabela utilizatorilor.
        """

        super().__init__(User)

    def get_by_username(self, username: str):
        """
        Returnează utilizatorul după username.
        """

        # Căutăm primul utilizator cu username-ul primit.
        return self.model.objects.filter(username=username).first()

    def get_instance_by_username(self, username: str):
        """
        Alias pentru get_by_username().

        Păstrat pentru:
        - compatibilitate,
        - cod mai vechi,
        - date default.
        """

        return self.get_by_username(username)

    def get_by_email(self, email: str):
        """
        Returnează utilizatorul după adresa de email.
        """

        return self.model.objects.filter(email=email).first()

    def get_user_by_username_or_email(self, username_or_email: str):
        """
        Caută utilizatorul fie după username,
        fie după email.

        Această metodă este utilă la login,
        unde utilizatorul poate introduce:
        - username
        - sau email.
        """

        return self.model.objects.filter(
            Q(username=username_or_email) | Q(email=username_or_email)
        ).first()

    def create_user(self, **data):
        """
        Creează un utilizator nou.

        IMPORTANT:
        Parola este hash-uită înainte de salvare.
        Nu salvăm niciodată parole în format text simplu.
        """

        # Extragem parola din datele primite.
        password = data.pop("password", None)

        # Creăm instanța utilizatorului fără salvare imediată.
        user = self.model(**data)

        # Dacă există parolă, o hash-uim securizat.
        if password:
            user.set_password(password)

        # Salvăm utilizatorul în baza de date.
        user.save()

        return user

    def get_or_create_google_user(self, email: str):
        """
        Returnează utilizatorul autentificat prin Google.

        Dacă utilizatorul nu există:
        - este creat automat.

        get_or_create() returnează:
        - obiectul găsit/creat
        - și un boolean care spune dacă a fost creat nou.
        """

        # Generăm username-ul folosind partea din email
        # dinainte de caracterul '@'.
        #
        # Exemplu:
        # alex@gmail.com -> alex
        username = email.split("@")[0]

        return self.model.objects.get_or_create(
            email=email,
            defaults={
                "username": username,
                "is_active": True,
            },
        )

    def username_exists_for_other_user(self, username: str, user_id: int) -> bool:
        """
        Verifică dacă username-ul există deja
        la alt utilizator.

        Folosim această metodă la editarea profilului
        pentru a evita duplicatele.
        """

        return self.model.objects.filter(username=username).exclude(id=user_id).exists()

    def update_profile_fields(
        self, user, username=None, first_name=None, last_name=None
    ):
        """
        Actualizează câmpurile profilului utilizatorului.

        Actualizăm doar valorile care sunt trimise.
        Dacă un câmp este None, îl lăsăm nemodificat.
        """

        # Actualizăm username-ul dacă există valoare nouă.
        if username is not None:
            user.username = username

        # Actualizăm prenumele.
        if first_name is not None:
            user.first_name = first_name

        # Actualizăm numele de familie.
        if last_name is not None:
            user.last_name = last_name

        # Salvăm modificările în baza de date.
        user.save()

        return user
