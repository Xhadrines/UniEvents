def default_notification_type_data():
    """
    Returnează lista tipurilor de notificări default
    utilizate în aplicație.

    Aceste tipuri sunt folosite pentru:
    - remindere,
    - confirmări,
    - actualizări,
    - anulări de evenimente.
    """

    return [
        # =====================================================
        # REMINDER
        # =====================================================
        {
            # Tip notificare reminder.
            "name": "Reminder",
            # Descriere notificare.
            "description": ("Reminder before an event starts."),
        },
        # =====================================================
        # REGISTRATION CONFIRMATION
        # =====================================================
        {
            # Confirmare înscriere.
            "name": "Registration Confirmation",
            # Descriere.
            "description": ("Confirmation after event registration."),
        },
        # =====================================================
        # EVENT UPDATE
        # =====================================================
        {
            # Actualizare eveniment.
            "name": "Event Update",
            # Descriere notificare.
            "description": ("Notification for event changes."),
        },
        # =====================================================
        # EVENT CANCELLED
        # =====================================================
        {
            # Eveniment anulat.
            "name": "Event Cancelled",
            # Descriere notificare.
            "description": ("Notification for cancelled events."),
        },
    ]
