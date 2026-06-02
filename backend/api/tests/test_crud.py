import unittest
from unittest.mock import ANY, MagicMock, call, patch, sentinel

from rest_framework import status
from rest_framework.test import APIRequestFactory

from api.views import (
    CategoryView,
    EmailTokenView,
    EventMaterialView,
    EventSponsorView,
    EventView,
    FacultyView,
    FavoriteEventView,
    FeedbackView,
    LocationView,
    MaterialTypeView,
    NotificationTypeView,
    NotificationView,
    OrganizerTypeView,
    OrganizerView,
    ParticipationTypeView,
    RegistrationView,
    ReportView,
    RoleView,
    SpecializationView,
    SponsorView,
    StatusView,
    UserProfileView,
)

# Lista tuturor view-urilor CRUD
# care trebuie testate automat.
#
# Practic:
# pentru fiecare view din această listă
# vor fi generate automat testele:
# - GET
# - POST
# - PUT
# - PATCH
# - DELETE
CRUD_TABLE_VIEWS = [
    CategoryView,
    EmailTokenView,
    EventMaterialView,
    EventSponsorView,
    EventView,
    FacultyView,
    FavoriteEventView,
    FeedbackView,
    LocationView,
    MaterialTypeView,
    NotificationTypeView,
    NotificationView,
    OrganizerTypeView,
    OrganizerView,
    ParticipationTypeView,
    RegistrationView,
    ReportView,
    RoleView,
    SpecializationView,
    SponsorView,
    StatusView,
    UserProfileView,
]


class BaseCRUDViewTests(unittest.TestCase):
    """
    Clasă de bază pentru testele CRUD.

    Folosim această clasă pentru:
    - reutilizarea logicii comune,
    - evitarea duplicării codului,
    - generarea automată a testelor.
    """

    def setUp(self):
        """
        Se execută înaintea fiecărui test.

        APIRequestFactory:
        - simulează request-uri HTTP,
        - fără a porni serverul real.
        """

        self.factory = APIRequestFactory()


def _test_get(view_class):
    """
    Generează automat testul GET
    pentru view-ul primit ca parametru.
    """

    def test_method(self):

        # Mock pentru service.
        service = MagicMock()

        # Simulăm obiectul returnat din baza de date.
        service.get_by_id.return_value = sentinel.obj

        # Mock pentru serializer-ul de output.
        output_serializer = MagicMock()

        # Datele care vor fi returnate în response.
        output_serializer.data = {"id": 1}

        # Mock pentru serializer class.
        serializer_class = MagicMock(return_value=output_serializer)

        # Înlocuim service-ul și serializer-ul real
        # cu mock-uri.
        with patch.object(view_class, "service", service), patch.object(
            view_class, "serializer_class", serializer_class
        ):

            # Simulăm request GET.
            response = view_class.as_view()(self.factory.get("/"), pk=1)

        # Verificăm status code-ul.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificăm dacă service-ul a fost apelat corect.
        service.get_by_id.assert_called_once_with(1)

        # Verificăm dacă serializer-ul a fost apelat corect.
        serializer_class.assert_called_once_with(
            sentinel.obj,
            context={"request": ANY},
        )

        # Verificăm datele returnate.
        self.assertEqual(response.data, {"id": 1})

    return test_method


def _test_post(view_class):
    """
    Generează automat testul POST
    pentru view-ul primit.
    """

    def test_method(self):

        # Mock pentru serializer-ul de input.
        input_serializer = MagicMock()

        # Simulăm validarea cu succes.
        input_serializer.is_valid.return_value = True

        # Simulăm obiectul creat.
        input_serializer.save.return_value = sentinel.created_obj

        # Mock pentru serializer-ul de output.
        output_serializer = MagicMock()
        output_serializer.data = {"id": 2}

        # side_effect:
        # primul apel -> input serializer
        # al doilea apel -> output serializer
        serializer_class = MagicMock(side_effect=[input_serializer, output_serializer])

        with patch.object(view_class, "serializer_class", serializer_class):

            # Simulăm request POST.
            response = view_class.as_view()(
                self.factory.post("/", {"name": "demo"}, format="json")
            )

        # Verificăm status code-ul.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verificăm dacă save() a fost apelat.
        input_serializer.save.assert_called_once_with()

        # Verificăm apelurile serializer-ului.
        serializer_class.assert_has_calls(
            [
                call(
                    data={"name": "demo"},
                    context={"request": ANY},
                ),
                call(
                    sentinel.created_obj,
                    context={"request": ANY},
                ),
            ]
        )

        # Verificăm răspunsul.
        self.assertEqual(response.data, {"id": 2})

    return test_method


def _test_put(view_class):
    """
    Generează automat testul PUT
    pentru view-ul primit.
    """

    def test_method(self):

        service = MagicMock()

        # Simulăm obiectul existent.
        service.get_by_id.return_value = sentinel.existing_obj

        # Mock pentru serializer-ul de input.
        input_serializer = MagicMock()
        input_serializer.is_valid.return_value = True

        # Simulăm obiectul actualizat.
        input_serializer.save.return_value = sentinel.updated_obj

        # Serializer pentru output.
        output_serializer = MagicMock()
        output_serializer.data = {"id": 3}

        serializer_class = MagicMock(side_effect=[input_serializer, output_serializer])

        with patch.object(view_class, "service", service), patch.object(
            view_class, "serializer_class", serializer_class
        ):

            # Simulăm request PUT.
            response = view_class.as_view()(
                self.factory.put("/", {"name": "updated"}, format="json"),
                pk=1,
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        service.get_by_id.assert_called_once_with(1)

        input_serializer.save.assert_called_once_with()

        serializer_class.assert_has_calls(
            [
                call(
                    sentinel.existing_obj,
                    data={"name": "updated"},
                    context={"request": ANY},
                ),
                call(
                    sentinel.updated_obj,
                    context={"request": ANY},
                ),
            ]
        )

        self.assertEqual(response.data, {"id": 3})

    return test_method


def _test_patch(view_class):
    """
    Generează automat testul PATCH
    pentru view-ul primit.
    """

    def test_method(self):

        service = MagicMock()
        service.get_by_id.return_value = sentinel.existing_obj

        input_serializer = MagicMock()
        input_serializer.is_valid.return_value = True
        input_serializer.save.return_value = sentinel.patched_obj

        output_serializer = MagicMock()
        output_serializer.data = {"id": 4}

        serializer_class = MagicMock(side_effect=[input_serializer, output_serializer])

        with patch.object(view_class, "service", service), patch.object(
            view_class, "serializer_class", serializer_class
        ):

            # Simulăm request PATCH.
            response = view_class.as_view()(
                self.factory.patch("/", {"name": "patched"}, format="json"),
                pk=1,
            )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        service.get_by_id.assert_called_once_with(1)

        input_serializer.save.assert_called_once_with()

        serializer_class.assert_has_calls(
            [
                call(
                    sentinel.existing_obj,
                    data={"name": "patched"},
                    partial=True,
                    context={"request": ANY},
                ),
                call(
                    sentinel.patched_obj,
                    context={"request": ANY},
                ),
            ]
        )

        self.assertEqual(response.data, {"id": 4})

    return test_method


def _test_delete(view_class):
    """
    Generează automat testul DELETE
    pentru view-ul primit.
    """

    def test_method(self):

        service = MagicMock()

        # Simulăm ștergerea cu succes.
        service.delete.return_value = True

        with patch.object(view_class, "service", service):

            # Simulăm request DELETE.
            response = view_class.as_view()(self.factory.delete("/"), pk=1)

        # DELETE reușit -> 204 NO CONTENT.
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        service.delete.assert_called_once_with(1)

    return test_method


# Generăm automat toate testele CRUD
# pentru fiecare view din listă.
for _view in CRUD_TABLE_VIEWS:

    # Construim numele testului.
    #
    # Exemplu:
    # CategoryView -> category
    _name = _view.__name__.replace("View", "").lower()

    # Adăugăm metodele generate dinamic în clasa de teste.
    setattr(BaseCRUDViewTests, f"test_{_name}_get", _test_get(_view))

    setattr(BaseCRUDViewTests, f"test_{_name}_post", _test_post(_view))

    setattr(BaseCRUDViewTests, f"test_{_name}_put", _test_put(_view))

    setattr(BaseCRUDViewTests, f"test_{_name}_patch", _test_patch(_view))

    setattr(BaseCRUDViewTests, f"test_{_name}_delete", _test_delete(_view))
