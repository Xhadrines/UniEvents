# Importăm configurația aplicației API.
#
# Acest import permite accesul rapid la clasa ApiConfig
# direct din pachetul curent.
#
# Practic:
# în loc de:
# from api.apps import ApiConfig
#
# putem folosi:
# from api import ApiConfig

from .apps import ApiConfig
