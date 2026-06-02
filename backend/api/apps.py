from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configurația aplicației Django "api".

    Această clasă este folosită de Django pentru:
    - identificarea aplicației,
    - încărcarea configurațiilor,
    - inițializarea componentelor aplicației.
    """

    # Numele aplicației Django.
    #
    # Acesta trebuie să coincidă cu numele folderului aplicației.
    name = "api"
