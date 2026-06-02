def default_participation_type_data():
    """
    Returnează lista tipurilor de participare default
    utilizate pentru evenimente.

    Aceste tipuri definesc modul în care
    participanții pot lua parte la eveniment.
    """

    return [
        # =====================================================
        # FIZIC
        # =====================================================
        {
            # Participare fizică.
            "name": "Fizic",
            # Descriere.
            "description": (
                "Participants attend the event " "at the physical location."
            ),
        },
        # =====================================================
        # ONLINE
        # =====================================================
        {
            # Participare online.
            "name": "Online",
            # Descriere.
            "description": (
                "Participants attend the event " "through an online platform."
            ),
        },
        # =====================================================
        # HIBRID
        # =====================================================
        {
            # Participare mixtă.
            "name": "Hibrid",
            # Descriere.
            "description": ("Participants can attend either " "physically or online."),
        },
    ]
