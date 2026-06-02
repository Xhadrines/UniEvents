# Importăm toate service-urile aplicației într-un singur loc.
#
# Scopul acestui fișier este să centralizeze importurile,
# astfel încât în alte părți ale proiectului să putem face:
#
# from services import UserService
#
# în loc de:
#
# from services.user import UserService
#
# Practic:
# - codul devine mai curat,
# - importurile sunt mai scurte,
# - pachetul services devine mai ușor de folosit.

from .base_service import BaseService
from .category import CategoryService
from .status import StatusService
from .role import RoleService
from .faculty import FacultyService
from .specialization import SpecializationService
from .participation_type import ParticipationTypeService
from .location import LocationService
from .organizer_type import OrganizerTypeService
from .organizer import OrganizerService
from .event import EventService
from .registration import RegistrationService
from .feedback import FeedbackService
from .material_type import MaterialTypeService
from .event_material import EventMaterialService
from .sponsor import SponsorService
from .event_sponsor import EventSponsorService
from .favorite_event import FavoriteEventService
from .notification_type import NotificationTypeService
from .notification import NotificationService
from .report import ReportService
from .user_profile import UserProfileService
from .email_token import EmailTokenService
from .email import EmailService
from .user import UserService
from .google_auth import GoogleAuthService
