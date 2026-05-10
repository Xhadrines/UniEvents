from datetime import datetime
from django.utils import timezone


def aware(year, month, day, hour, minute=0):
    # Creeaza o data timezone-aware
    return timezone.make_aware(datetime(year, month, day, hour, minute, 0))
