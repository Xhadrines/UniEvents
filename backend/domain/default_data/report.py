from api.repository import UserRepository


def default_report_data():
    """
    Returnează datele default pentru rapoarte.

    Aceste rapoarte sunt utilizate pentru:
    - administrare,
    - analiză statistică,
    - monitorizarea activității organizatorilor,
    - testare și dezvoltare.
    """

    # Inițializăm repository-ul utilizatorilor.
    user_repository = UserRepository()

    return [
        # =====================================================
        # MONTHLY EVENTS REPORT
        # =====================================================
        {
            # Utilizatorul care a generat raportul.
            "generated_by": (user_repository.get_instance_by_username("administrator")),
            # Titlul raportului.
            "title": "Monthly Events Report",
            # Descriere raport.
            "description": (
                "Report containing number of events, "
                "average participation and organizer activity."
            ),
            # Fișierul asociat raportului.
            "file": ("reports/monthly_events_report.pdf"),
        },
        # =====================================================
        # ORGANIZER ACTIVITY REPORT
        # =====================================================
        {
            # Administratorul care a generat raportul.
            "generated_by": (user_repository.get_instance_by_username("administrator")),
            # Titlul raportului.
            "title": "Organizer Activity Report",
            # Descriere.
            "description": ("Report for events organized by FIRESC."),
            # Fișier PDF asociat.
            "file": ("reports/organizer_firesc_report.pdf"),
        },
    ]
