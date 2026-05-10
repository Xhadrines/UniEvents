from api.repository import UserRepository


def default_report_data():
    user_repository = UserRepository()

    return [
        {
            "generated_by": user_repository.get_instance_by_username("administrator"),
            "title": "Monthly Events Report",
            "description": "Report containing number of events, average participation and organizer activity.",
            "file": "reports/monthly_events_report.pdf",
        },
        {
            "generated_by": user_repository.get_instance_by_username("administrator"),
            "title": "Organizer Activity Report",
            "description": "Report for events organized by FIRESC.",
            "file": "reports/organizer_firesc_report.pdf",
        },
    ]
