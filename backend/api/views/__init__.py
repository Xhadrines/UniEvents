from .home import HomeView
from .base_crud import BaseCRUDView
from .category import CategoryView
from .status import StatusView
from .role import RoleView, AdminRoleRequestView
from .faculty import FacultyView
from .specialization import SpecializationView
from .participation_type import ParticipationTypeView
from .location import LocationView
from .organizer_type import OrganizerTypeView
from .organizer import OrganizerView
from .material_type import MaterialTypeView
from .sponsor import SponsorView
from .event_sponsor import EventSponsorView
from .notification_type import NotificationTypeView
from .report import ReportView
from .email_token import EmailTokenView
from .event import (
    EventView,
    UpcomingEventsView,
    ValidateEventView,
    CancelEventView,
    RejectEventView,
    AcceptedEventsView,
)
from .registration import (
    RegistrationView,
    RegisterToEventView,
    CancelRegistrationView,
    CheckInView,
)
from .feedback import FeedbackView, AddFeedbackView, EventFeedbackListView
from .event_material import (
    EventMaterialView,
    EventMaterialsByEventView,
    UploadEventMaterialView,
)
from .favorite_event import (
    FavoriteEventView,
    MyFavoriteEventsView,
    AddFavoriteEventView,
    RemoveFavoriteEventView,
)
from .notification import (
    NotificationView,
    MyNotificationsView,
    UnreadNotificationsView,
    MarkNotificationAsReadView,
)
from .user_profile import UserProfileView, CompleteProfileView, MyProfileUpdateView
from .user import (
    UserView,
    RegisterView,
    LoginView,
    PasswordResetRequestView,
    PasswordResetConfirmView,
)
from .google_auth import GoogleAuthView
