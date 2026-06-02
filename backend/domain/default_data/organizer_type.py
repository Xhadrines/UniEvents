def default_organizer_type_data():
    """
    Returnează lista tipurilor de organizatori default
    utilizate în aplicație.

    Aceste tipuri sunt folosite pentru clasificarea
    organizatorilor evenimentelor universitare.
    """

    return [
        # =====================================================
        # ASOCIATIE STUDENTEASCA
        # =====================================================
        {
            # Numele tipului de organizator.
            "name": "Asociatie de studenti",
            # Descriere.
            "description": (
                "Student association that organizes " "events for students."
            ),
        },
        # =====================================================
        # PROFESOR
        # =====================================================
        {
            # Organizator de tip profesor.
            "name": "Profesor",
            # Descriere.
            "description": ("Teacher or academic staff organizer."),
        },
        # =====================================================
        # CLUB UNIVERSITAR
        # =====================================================
        {
            # Club universitar.
            "name": "Club universitar",
            # Descriere.
            "description": (
                "University club that organizes " "academic or social activities."
            ),
        },
        # =====================================================
        # PARTENER EXTERN
        # =====================================================
        {
            # Companie sau instituție externă.
            "name": "Partener extern",
            # Descriere.
            "description": (
                "External company or institution " "involved in university events."
            ),
        },
        # =====================================================
        # STRUCTURA UNIVERSITARA
        # =====================================================
        {
            # Structură oficială a universității.
            "name": "Structura universitara",
            # Descriere.
            "description": (
                "Official university structure, "
                "faculty, department, center or office."
            ),
        },
        # =====================================================
        # INSTITUTIE PUBLICA
        # =====================================================
        {
            # Instituție publică.
            "name": "Institutie publica",
            # Descriere.
            "description": (
                "Public institution involved in " "academic, cultural or civic events."
            ),
        },
    ]
