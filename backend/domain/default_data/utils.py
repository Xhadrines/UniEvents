from datetime import datetime

from django.utils import timezone


def aware(year, month, day, hour, minute=0):
    """
    Creează și returnează un obiect datetime
    timezone-aware utilizat în aplicație.

    Funcția este folosită pentru:
    - evenimente,
    - notificări,
    - înregistrări,
    - seed data,
    - testare.
    """

    # =====================================================
    # CREATE NAIVE DATETIME
    # =====================================================

    naive_datetime = datetime(
        year,
        month,
        day,
        hour,
        minute,
        0,
    )

    # =====================================================
    # CONVERT TO TIMEZONE-AWARE DATETIME
    # =====================================================

    return timezone.make_aware(naive_datetime)
