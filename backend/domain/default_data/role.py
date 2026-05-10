def default_role_data():
    return [
        {
            "name": "Administrator",
            "description": "Role with full permissions for users, events, reports and validations.",
        },
        {
            "name": "Student",
            "description": "Role for students who can view events, register and add feedback.",
        },
        {
            "name": "Profesor",
            "description": "Role for teachers who can organize university events.",
        },
        {
            "name": "Partener",
            "description": "Role for external partners involved in events and sponsorships.",
        },
        {
            "name": "Organizatie",
            "description": "Role for student associations, clubs and organizations.",
        },
        {
            "name": "Altele",
            "description": "Generic role for users that do not match the standard categories.",
        },
    ]
