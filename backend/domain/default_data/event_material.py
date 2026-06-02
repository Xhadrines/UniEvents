from api.repository import (
    UserRepository,
    EventRepository,
    MaterialTypeRepository,
)


def default_event_material_data():
    """
    Returnează datele default pentru materialele evenimentelor.

    Aceste date sunt folosite pentru:
    - seed-ul inițial al bazei de date,
    - dezvoltare,
    - testare.
    """

    # Inițializăm repository-urile necesare.
    user_repository = UserRepository()

    event_repository = EventRepository()

    material_type_repository = MaterialTypeRepository()

    # Obținem evenimentul AI.
    ai_event = event_repository.get_instance_by_name(
        "Workshop Introducere in Inteligenta Artificiala"
    )

    return [
        # =====================================================
        # DOCUMENT PDF
        # =====================================================
        {
            # Evenimentul asociat materialului.
            "event": ai_event,
            # Tipul materialului.
            "material_type": (material_type_repository.get_instance_by_name("PDF")),
            # Titlul materialului.
            "title": "AI Workshop Support Document",
            # Calea către fișier.
            #
            # De regulă:
            # media/event_materials/...
            "file": ("event_materials/" "ai_workshop_support.pdf"),
            # Materialul este public.
            "is_public": True,
            # Utilizatorul care a încărcat materialul.
            "uploaded_by": (user_repository.get_instance_by_username("professor")),
        },
        # =====================================================
        # PREZENTARE
        # =====================================================
        {
            # Evenimentul asociat materialului.
            "event": ai_event,
            # Tipul materialului:
            # prezentare / slides.
            "material_type": (
                material_type_repository.get_instance_by_name("Presentation")
            ),
            # Titlul prezentării.
            "title": ("Introduction to Machine Learning Slides"),
            # Fișierul asociat.
            "file": ("event_materials/" "ml_intro_slides.pdf"),
            # Material public.
            "is_public": True,
            # Utilizatorul care a încărcat materialul.
            "uploaded_by": (user_repository.get_instance_by_username("organization")),
        },
    ]
