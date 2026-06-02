def default_material_type_data():
    """
    Returnează lista tipurilor de materiale default
    utilizate în aplicație.

    Aceste tipuri sunt folosite pentru:
    - materialele evenimentelor,
    - resurse educaționale,
    - documente încărcate.
    """

    return [
        # =====================================================
        # PDF
        # =====================================================
        {
            # Numele tipului de material.
            "name": "PDF",
            # Descrierea tipului.
            "description": "PDF document.",
        },
        # =====================================================
        # PRESENTATION
        # =====================================================
        {
            # Tip material:
            # prezentare / slides.
            "name": "Presentation",
            # Descriere.
            "description": ("Slides or presentation file."),
        },
        # =====================================================
        # IMAGE
        # =====================================================
        {
            # Tip material imagine.
            "name": "Image",
            # Descriere.
            "description": "Image file.",
        },
        # =====================================================
        # ARCHIVE
        # =====================================================
        {
            # Tip material arhivă.
            "name": "Archive",
            # Descriere.
            "description": ("Compressed archive with resources."),
        },
    ]
