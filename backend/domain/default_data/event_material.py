from api.repository import UserRepository, EventRepository, MaterialTypeRepository


def default_event_material_data():
    user_repository = UserRepository()
    event_repository = EventRepository()
    material_type_repository = MaterialTypeRepository()

    ai_event = event_repository.get_instance_by_name(
        "Workshop Introducere in Inteligenta Artificiala"
    )

    return [
        {
            "event": ai_event,
            "material_type": material_type_repository.get_instance_by_name("PDF"),
            "title": "AI Workshop Support Document",
            "file": "event_materials/ai_workshop_support.pdf",
            "is_public": True,
            "uploaded_by": user_repository.get_instance_by_username("professor"),
        },
        {
            "event": ai_event,
            "material_type": material_type_repository.get_instance_by_name(
                "Presentation"
            ),
            "title": "Introduction to Machine Learning Slides",
            "file": "event_materials/ml_intro_slides.pdf",
            "is_public": True,
            "uploaded_by": user_repository.get_instance_by_username("organization"),
        },
    ]
