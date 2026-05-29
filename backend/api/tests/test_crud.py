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
    def setUp(self):
        self.factory = APIRequestFactory()


def _test_get(view_class):
    def test_method(self):
        service = MagicMock()
        service.get_by_id.return_value = sentinel.obj

        output_serializer = MagicMock()
        output_serializer.data = {"id": 1}
        serializer_class = MagicMock(return_value=output_serializer)

        with patch.object(view_class, "service", service), patch.object(
            view_class, "serializer_class", serializer_class
        ):
            response = view_class.as_view()(self.factory.get("/"), pk=1)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        service.get_by_id.assert_called_once_with(1)
        serializer_class.assert_called_once_with(
            sentinel.obj,
            context={"request": ANY},
        )
        self.assertEqual(response.data, {"id": 1})

    return test_method


def _test_post(view_class):
    def test_method(self):
        input_serializer = MagicMock()
        input_serializer.is_valid.return_value = True
        input_serializer.save.return_value = sentinel.created_obj

        output_serializer = MagicMock()
        output_serializer.data = {"id": 2}

        serializer_class = MagicMock(side_effect=[input_serializer, output_serializer])

        with patch.object(view_class, "serializer_class", serializer_class):
            response = view_class.as_view()(
                self.factory.post("/", {"name": "demo"}, format="json")
            )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        input_serializer.save.assert_called_once_with()
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
        self.assertEqual(response.data, {"id": 2})

    return test_method


def _test_put(view_class):
    def test_method(self):
        service = MagicMock()
        service.get_by_id.return_value = sentinel.existing_obj

        input_serializer = MagicMock()
        input_serializer.is_valid.return_value = True
        input_serializer.save.return_value = sentinel.updated_obj

        output_serializer = MagicMock()
        output_serializer.data = {"id": 3}

        serializer_class = MagicMock(side_effect=[input_serializer, output_serializer])

        with patch.object(view_class, "service", service), patch.object(
            view_class, "serializer_class", serializer_class
        ):
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
    def test_method(self):
        service = MagicMock()
        service.delete.return_value = True

        with patch.object(view_class, "service", service):
            response = view_class.as_view()(self.factory.delete("/"), pk=1)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        service.delete.assert_called_once_with(1)

    return test_method


for _view in CRUD_TABLE_VIEWS:
    _name = _view.__name__.replace("View", "").lower()

    setattr(BaseCRUDViewTests, f"test_{_name}_get", _test_get(_view))
    setattr(BaseCRUDViewTests, f"test_{_name}_post", _test_post(_view))
    setattr(BaseCRUDViewTests, f"test_{_name}_put", _test_put(_view))
    setattr(BaseCRUDViewTests, f"test_{_name}_patch", _test_patch(_view))
    setattr(BaseCRUDViewTests, f"test_{_name}_delete", _test_delete(_view))
