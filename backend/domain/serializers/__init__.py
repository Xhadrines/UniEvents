"""
Import centralizat pentru toate serializer-ele aplicației.

Acest fișier permite:
- importuri mai simple,
- acces rapid la toate serializer-ele,
- organizare mai bună a layer-ului API,
- evitarea importurilor repetitive.

Exemplu:
    from domain.serializers import (
        EventSerializer,
        OrganizerSerializer,
    )
"""

# =====================================================
# BASE SERIALIZER
# =====================================================

# Serializer de bază reutilizat
# de celelalte serializer-e.
from .base_serializer import BaseSerializer

# =====================================================
# CORE ENTITIES
# =====================================================

# Serializer pentru categorii.
from .category import CategorySerializer

# Serializer pentru statusuri.
from .status import StatusSerializer

# Serializer pentru roluri.
from .role import RoleSerializer

# Serializer pentru facultăți.
from .faculty import FacultySerializer

# Serializer pentru specializări.
from .specialization import SpecializationSerializer

# Serializer pentru tipuri de participare.
from .participation_type import ParticipationTypeSerializer

# =====================================================
# LOCATION DOMAIN
# =====================================================

# Serializer pentru locații.
from .location import LocationSerializer

# =====================================================
# ORGANIZER DOMAIN
# =====================================================

# Serializer pentru tipuri organizatori.
from .organizer_type import OrganizerTypeSerializer

# Serializer pentru organizatori.
from .organizer import OrganizerSerializer

# =====================================================
# EVENT DOMAIN
# =====================================================

# Serializer pentru evenimente.
from .event import EventSerializer

# Serializer pentru înscrieri.
from .registration import RegistrationSerializer

# Serializer pentru feedback.
from .feedback import FeedbackSerializer

# =====================================================
# EVENT MATERIALS
# =====================================================

# Serializer pentru tipuri materiale.
from .material_type import MaterialTypeSerializer

# Serializer pentru materiale eveniment.
from .event_material import EventMaterialSerializer

# =====================================================
# SPONSORS
# =====================================================

# Serializer pentru sponsori.
from .sponsor import SponsorSerializer

# Serializer pentru relația
# sponsor-eveniment.
from .event_sponsor import EventSponsorSerializer

# =====================================================
# FAVORITES
# =====================================================

# Serializer pentru evenimente favorite.
from .favorite_event import FavoriteEventSerializer

# =====================================================
# NOTIFICATIONS
# =====================================================

# Serializer pentru tipuri notificări.
from .notification_type import NotificationTypeSerializer

# Serializer pentru notificări.
from .notification import NotificationSerializer

# =====================================================
# REPORTS
# =====================================================

# Serializer pentru rapoarte.
from .report import ReportSerializer

# =====================================================
# USER DOMAIN
# =====================================================

# Serializer pentru profil utilizator.
from .user_profile import UserProfileSerializer

# Serializer pentru token-uri email.
from .email_token import EmailTokenSerializer

# Serializer pentru utilizatori.
from .user import UserSerializer
