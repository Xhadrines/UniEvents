def default_status_data():
    """
    Returnează lista statusurilor default
    utilizate în aplicație.

    Statusurile sunt folosite pentru:
    - utilizatori,
    - evenimente,
    - înscrieri,
    - notificări,
    - procese administrative.
    """

    return [
        # =====================================================
        # ACTIV
        # =====================================================
        {
            # Status activ.
            "name": "Activ",
            # Descriere.
            "description": ("Entity is active and can be used."),
        },
        # =====================================================
        # INACTIV
        # =====================================================
        {
            # Status inactiv.
            "name": "Inactiv",
            # Descriere.
            "description": ("Entity is inactive but can be reactivated."),
        },
        # =====================================================
        # STERS
        # =====================================================
        {
            # Entitate marcată ca ștearsă.
            "name": "Sters",
            # Descriere.
            "description": ("Entity is marked as deleted."),
        },
        # =====================================================
        # IN ASTEPTARE
        # =====================================================
        {
            # Status pending / awaiting approval.
            "name": "In asteptare",
            # Descriere.
            "description": ("Entity is waiting for validation " "or approval."),
        },
        # =====================================================
        # ANULAT
        # =====================================================
        {
            # Status anulat.
            "name": "Anulat",
            # Descriere.
            "description": ("Entity was cancelled."),
        },
        # =====================================================
        # RESPINS
        # =====================================================
        {
            # Status respins.
            "name": "Respins",
            # Descriere.
            "description": ("Entity was rejected."),
        },
        # =====================================================
        # ACCEPTAT
        # =====================================================
        {
            # Status acceptat.
            "name": "Acceptat",
            # Descriere.
            "description": ("Entity was accepted or approved."),
        },
        # =====================================================
        # LISTA DE ASTEPTARE
        # =====================================================
        {
            # Waiting list.
            "name": "Lista de asteptare",
            # Descriere.
            "description": ("Registration is placed on the " "waiting list."),
        },
        # =====================================================
        # FINALIZAT
        # =====================================================
        {
            # Proces sau eveniment finalizat.
            "name": "Finalizat",
            # Descriere.
            "description": ("Event or process is finished."),
        },
    ]
