def default_role_data():
    """
    Returnează lista rolurilor default
    utilizate în aplicație.

    Rolurile definesc nivelul de acces
    și permisiunile utilizatorilor.
    """

    return [
        # =====================================================
        # ADMINISTRATOR
        # =====================================================
        {
            # Numele rolului.
            "name": "Administrator",
            # Descriere rol.
            "description": (
                "Role with full permissions for users, "
                "events, reports and validations."
            ),
        },
        # =====================================================
        # STUDENT
        # =====================================================
        {
            # Rol student.
            "name": "Student",
            # Permisiuni specifice studentului.
            "description": (
                "Role for students who can view events, " "register and add feedback."
            ),
        },
        # =====================================================
        # PROFESOR
        # =====================================================
        {
            # Rol profesor.
            "name": "Profesor",
            # Permisiuni profesor.
            "description": ("Role for teachers who can organize " "university events."),
        },
        # =====================================================
        # PARTENER
        # =====================================================
        {
            # Partener extern.
            "name": "Partener",
            # Descriere.
            "description": (
                "Role for external partners involved " "in events and sponsorships."
            ),
        },
        # =====================================================
        # ORGANIZATIE
        # =====================================================
        {
            # Organizații studențești / cluburi.
            "name": "Organizatie",
            # Descriere.
            "description": (
                "Role for student associations, " "clubs and organizations."
            ),
        },
        # =====================================================
        # ALTELE
        # =====================================================
        {
            # Rol generic.
            "name": "Altele",
            # Descriere.
            "description": (
                "Generic role for users that do not " "match the standard categories."
            ),
        },
    ]
