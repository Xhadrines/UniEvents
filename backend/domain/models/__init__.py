"""
Import centralizat pentru toate modelele aplicației.

Acest fișier permite:
- importuri mai simple,
- acces rapid la toate modelele,
- organizare mai bună a layer-ului domain,
- evitarea importurilor repetitive.

Exemplu:
    from domain.models import Event, Organizer
"""

# =====================================================
# BASE MODEL
# =====================================================

# Model de bază utilizat pentru moștenire.
#
# Conține câmpuri și funcționalități comune:
# - created_at
# - updated_at
# - id
# - metode reutilizabile
from .base_model import BaseModel

# =====================================================
# CORE ENTITIES
# =====================================================

# Categoria evenimentelor.
from .category import Category

# Status generic:
# activ, inactiv, acceptat etc.
from .status import Status

# Tip participare:
# fizic, online, hibrid.
from .participation_type import ParticipationType

# Rol utilizator:
# administrator, student etc.
from .role import Role

# Facultate universitară.
from .faculty import Faculty

# Specializare asociată unei facultăți.
from .specialization import Specialization

# =====================================================
# USER DOMAIN
# =====================================================

# Profil extins utilizator.
#
# Include:
# - facultate
# - specializare
# - rol
# - status
# - date academice
from .user_profile import UserProfile

# =====================================================
# LOCATION DOMAIN
# =====================================================

# Locații pentru evenimente:
# săli, laboratoare, online etc.
from .location import Location

# =====================================================
# ORGANIZER DOMAIN
# =====================================================

# Tip organizator:
# profesor, organizație, partener etc.
from .organizer_type import OrganizerType

# Organizator eveniment.
from .organizer import Organizer

# =====================================================
# EVENT DOMAIN
# =====================================================

# Model principal pentru evenimente.
from .event import Event

# Înscriere utilizator la eveniment.
from .registration import Registration

# Feedback pentru evenimente.
from .feedback import Feedback

# =====================================================
# EVENT MATERIALS
# =====================================================

# Tip material:
# PDF, imagine, prezentare etc.
from .material_type import MaterialType

# Material asociat unui eveniment.
from .event_material import EventMaterial

# =====================================================
# SPONSORS
# =====================================================

# Sponsor eveniment.
from .sponsor import Sponsor

# Relație many-to-many:
# sponsor <-> eveniment
from .event_sponsor import EventSponsor

# =====================================================
# FAVORITES
# =====================================================

# Evenimente favorite ale utilizatorilor.
from .favorite_event import FavoriteEvent

# =====================================================
# NOTIFICATIONS
# =====================================================

# Tip notificare:
# reminder, update etc.
from .notification_type import NotificationType

# Notificare utilizator.
from .notification import Notification

# =====================================================
# REPORTS
# =====================================================

# Raport generat în aplicație.
from .report import Report

# =====================================================
# EMAIL TOKENS
# =====================================================

# Token utilizat pentru:
# - verificare email
# - completare profil
# - validare cont
from .email_token import EmailToken
