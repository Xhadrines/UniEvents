from api.repository import (
    UserRepository,
    RoleRepository,
    StatusRepository,
    FacultyRepository,
    SpecializationRepository,
)


def default_user_profile_data():
    """
    Returnează datele default pentru profilurile
    utilizatorilor din aplicație.

    Profilurile sunt utilizate pentru:
    - autentificare și autorizare,
    - asocierea rolurilor,
    - informații academice,
    - integrarea cu Google OAuth.
    """

    # =====================================================
    # REPOSITORIES
    # =====================================================

    user_repository = UserRepository()

    role_repository = RoleRepository()

    status_repository = StatusRepository()

    faculty_repository = FacultyRepository()

    specialization_repository = SpecializationRepository()

    # =====================================================
    # STATUS
    # =====================================================

    active_status = status_repository.get_instance_by_name("Activ")

    # =====================================================
    # FACULTATE + SPECIALIZARE
    # =====================================================

    faculty = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Electrica " "si Stiinta Calculatoarelor"
    )

    specialization = specialization_repository.get_instance_by_name("Calculatoare")

    return [
        # =====================================================
        # ADMINISTRATOR
        # =====================================================
        {
            # Utilizator asociat profilului.
            "user": (user_repository.get_instance_by_username("administrator")),
            # Rol administrator.
            "role": (role_repository.get_instance_by_name("Administrator")),
            # Status activ.
            "status": active_status,
        },
        # =====================================================
        # STUDENT
        # =====================================================
        {
            # Utilizator student.
            "user": (user_repository.get_instance_by_username("student")),
            # Rol student.
            "role": (role_repository.get_instance_by_name("Student")),
            # Status activ.
            "status": active_status,
            # Facultatea studentului.
            "faculty": faculty,
            # Specializarea studentului.
            "specialization": specialization,
            # An de studiu.
            "study_year": 1,
            # Grupă.
            "group": 1,
            # Semigrupă.
            "semi_group": "A",
            # Google OAuth subject ID.
            "google_sub": ("default-google-student-sub"),
            # Cont Google student.
            "is_google_student": True,
        },
        # =====================================================
        # PROFESOR
        # =====================================================
        {
            # Utilizator profesor.
            "user": (user_repository.get_instance_by_username("professor")),
            # Rol profesor.
            "role": (role_repository.get_instance_by_name("Profesor")),
            # Status activ.
            "status": active_status,
            # Facultate asociată.
            "faculty": faculty,
        },
        # =====================================================
        # PARTENER
        # =====================================================
        {
            # Utilizator partener extern.
            "user": (user_repository.get_instance_by_username("partner")),
            # Rol partener.
            "role": (role_repository.get_instance_by_name("Partener")),
            # Status activ.
            "status": active_status,
        },
        # =====================================================
        # ORGANIZATIE
        # =====================================================
        {
            # Utilizator organizație.
            "user": (user_repository.get_instance_by_username("organization")),
            # Rol organizație.
            "role": (role_repository.get_instance_by_name("Organizatie")),
            # Status activ.
            "status": active_status,
        },
        # =====================================================
        # GUEST
        # =====================================================
        {
            # Utilizator generic / guest.
            "user": (user_repository.get_instance_by_username("guest")),
            # Rol generic.
            "role": (role_repository.get_instance_by_name("Altele")),
            # Status activ.
            "status": active_status,
        },
    ]
