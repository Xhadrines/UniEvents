# Importăm clasele și constantele comune folosite în testele CRUD.
#
# BaseCRUDViewTests:
# - conține logica de bază reutilizabilă pentru testarea endpoint-urilor CRUD
# - evită duplicarea codului în mai multe fișiere de teste
#
# CRUD_TABLE_VIEWS:
# - conține lista endpoint-urilor/tabelelor
#   care trebuie testate automat.

from .test_crud import BaseCRUDViewTests, CRUD_TABLE_VIEWS
