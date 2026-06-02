from api.repository import (
    UserRepository,
    StatusRepository,
    OrganizerTypeRepository,
    FacultyRepository,
)


def default_organizer_data():
    """
    Returnează datele default pentru organizatori.

    Aceste date sunt utilizate pentru:
    - popularea inițială a bazei de date,
    - dezvoltare,
    - testare.
    """

    # =====================================================
    # REPOSITORIES
    # =====================================================

    user_repository = UserRepository()

    status_repository = StatusRepository()

    organizer_type_repository = OrganizerTypeRepository()

    faculty_repository = FacultyRepository()

    # =====================================================
    # STATUS
    # =====================================================

    active_status = status_repository.get_instance_by_name("Activ")

    # =====================================================
    # FACULTATI
    # =====================================================

    fiesc = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Electrica " "si Stiinta Calculatoarelor"
    )

    fdsa = faculty_repository.get_instance_by_name(
        "Facultatea de Drept " "si Stiinte Administrative"
    )

    feea = faculty_repository.get_instance_by_name(
        "Facultatea de Economie, " "Administratie si Afaceri"
    )

    fefs = faculty_repository.get_instance_by_name(
        "Facultatea de Educatie Fizica si Sport"
    )

    fia = faculty_repository.get_instance_by_name("Facultatea de Inginerie Alimentara")

    fimar = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Mecanica, " "Autovehicule si Robotica"
    )

    figs = faculty_repository.get_instance_by_name(
        "Facultatea de Istorie, Geografie " "si Stiinte Sociale"
    )

    flsc = faculty_repository.get_instance_by_name(
        "Facultatea de Litere " "si Stiinte ale Comunicarii"
    )

    fmsb = faculty_repository.get_instance_by_name(
        "Facultatea de Medicina " "si Stiinte Biologice"
    )

    fpse = faculty_repository.get_instance_by_name(
        "Facultatea de Psihologie " "si Stiinte ale Educatiei"
    )

    fs = faculty_repository.get_instance_by_name("Facultatea de Silvicultura")

    # =====================================================
    # TIPURI ORGANIZATORI
    # =====================================================

    student_association = organizer_type_repository.get_instance_by_name(
        "Asociatie de studenti"
    )

    professor = organizer_type_repository.get_instance_by_name("Profesor")

    university_club = organizer_type_repository.get_instance_by_name("Club universitar")

    external_partner = organizer_type_repository.get_instance_by_name("Partener extern")

    university_structure = organizer_type_repository.get_instance_by_name(
        "Structura universitara"
    )

    public_institution = organizer_type_repository.get_instance_by_name(
        "Institutie publica"
    )

    return [
        # =====================================================
        # FIRESC
        # =====================================================
        {
            "name": "FIRESC",
            "description": (
                "Asociatia studenteasca FIRESC "
                "din cadrul FIESC, implicata in "
                "evenimente, workshop-uri si "
                "activitati pentru studenti."
            ),
            "link": ("https://www.facebook.com/firesc"),
            "organizer_type": student_association,
            "user": (user_repository.get_instance_by_username("organization_firesc")),
            "status": active_status,
            "faculty": fiesc,
        },
        # =====================================================
        # ASUS
        # =====================================================
        {
            "name": "ASUS",
            "description": (
                "Asociatia Studentilor din "
                "Universitatea Suceava, implicata "
                "in reprezentarea studentilor si "
                "organizarea de activitati studentesti."
            ),
            "link": ("https://www.facebook.com/ASUS.Suceava"),
            "organizer_type": student_association,
            "user": (user_repository.get_instance_by_username("organization_asus")),
            "status": active_status,
            "faculty": None,
        },
        # =====================================================
        # AIESEC
        # =====================================================
        {
            "name": "AIESEC Suceava",
            "description": (
                "Organizatie studenteasca internationala "
                "orientata spre leadership, voluntariat "
                "si proiecte pentru tineri."
            ),
            "link": "https://aiesec.org",
            "organizer_type": student_association,
            "user": (user_repository.get_instance_by_username("organization_aiesec")),
            "status": active_status,
            "faculty": None,
        },
        # =====================================================
        # ANSSA
        # =====================================================
        {
            "name": "ANSSA",
            "description": (
                "Asociatia Nationala a Studentilor " "in Stiinte Administrative."
            ),
            "link": "https://www.facebook.com",
            "organizer_type": student_association,
            "user": (user_repository.get_instance_by_username("organization_anssa")),
            "status": active_status,
            "faculty": fdsa,
        },
        # =====================================================
        # ASCOR
        # =====================================================
        {
            "name": "ASCOR Suceava",
            "description": (
                "Asociatia Studentilor Crestini " "Ortodocsi Romani - filiala Suceava."
            ),
            "link": "https://www.facebook.com",
            "organizer_type": student_association,
            "user": (user_repository.get_instance_by_username("organization_ascor")),
            "status": active_status,
            "faculty": None,
        },
        # =====================================================
        # ARCANUL
        # =====================================================
        {
            "name": "Ansamblul Studentesc Arcanul",
            "description": (
                "Ansamblu studentesc dedicat " "activitatilor culturale si artistice."
            ),
            "link": "https://www.facebook.com",
            "organizer_type": university_club,
            "user": (user_repository.get_instance_by_username("organization_arcanul")),
            "status": active_status,
            "faculty": None,
        },
        # =====================================================
        # FIESC
        # =====================================================
        {
            "name": ("Facultatea de Inginerie Electrica " "si Stiinta Calculatoarelor"),
            "description": (
                "Facultate USV care organizeaza "
                "conferinte, workshop-uri si "
                "evenimente tehnice."
            ),
            "link": "https://fiesc.usv.ro",
            "organizer_type": university_structure,
            "user": (user_repository.get_instance_by_username("organization_fiesc")),
            "status": active_status,
            "faculty": fiesc,
        },
        # =====================================================
        # ASSIST SOFTWARE
        # =====================================================
        {
            "name": "ASSIST Software",
            "description": (
                "Companie IT din Suceava, "
                "partener educational si "
                "organizator de workshop-uri "
                "si internship-uri."
            ),
            "link": ("https://assist-software.net"),
            "organizer_type": external_partner,
            "user": (user_repository.get_instance_by_username("organization_assist")),
            "status": active_status,
            "faculty": fiesc,
        },
        # =====================================================
        # CONSILIUL JUDETEAN
        # =====================================================
        {
            "name": "Consiliul Judetean Suceava",
            "description": (
                "Institutie publica locala "
                "care colaboreaza cu USV "
                "in proiecte si evenimente."
            ),
            "link": ("https://www.cjsuceava.ro"),
            "organizer_type": public_institution,
            "user": (
                user_repository.get_instance_by_username("organization_cj_suceava")
            ),
            "status": active_status,
            "faculty": None,
        },
        # =====================================================
        # COMPUTER SCIENCE DEPARTMENT
        # =====================================================
        {
            "name": ("USV Computer Science Department"),
            "description": (
                "Academic department that organizes "
                "technical conferences and workshops."
            ),
            "link": "https://usv.ro",
            "organizer_type": professor,
            "user": (user_repository.get_instance_by_username("professor")),
            "status": active_status,
            "faculty": fiesc,
        },
    ]
