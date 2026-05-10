from api.repository import (
    UserRepository,
    RoleRepository,
    StatusRepository,
    FacultyRepository,
    SpecializationRepository,
)


def default_user_profile_data():
    user_repository = UserRepository()
    role_repository = RoleRepository()
    status_repository = StatusRepository()
    faculty_repository = FacultyRepository()
    specialization_repository = SpecializationRepository()

    active_status = status_repository.get_instance_by_name("Activ")

    faculty = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Electrica si Stiinta Calculatoarelor"
    )
    specialization = specialization_repository.get_instance_by_name("Calculatoare")

    return [
        {
            "user": user_repository.get_instance_by_username("administrator"),
            "role": role_repository.get_instance_by_name("Administrator"),
            "status": active_status,
        },
        {
            "user": user_repository.get_instance_by_username("student"),
            "role": role_repository.get_instance_by_name("Student"),
            "status": active_status,
            "faculty": faculty,
            "specialization": specialization,
            "study_year": 1,
            "group": 1,
            "semi_group": "A",
            "google_sub": "default-google-student-sub",
            "is_google_student": True,
        },
        {
            "user": user_repository.get_instance_by_username("professor"),
            "role": role_repository.get_instance_by_name("Profesor"),
            "status": active_status,
            "faculty": faculty,
        },
        {
            "user": user_repository.get_instance_by_username("partner"),
            "role": role_repository.get_instance_by_name("Partener"),
            "status": active_status,
        },
        {
            "user": user_repository.get_instance_by_username("organization"),
            "role": role_repository.get_instance_by_name("Organizatie"),
            "status": active_status,
        },
        {
            "user": user_repository.get_instance_by_username("guest"),
            "role": role_repository.get_instance_by_name("Altele"),
            "status": active_status,
        },
    ]
