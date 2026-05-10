from api.repository import (
    UserRepository,
    StatusRepository,
    OrganizerTypeRepository,
    FacultyRepository,
)


def default_organizer_data():
    user_repository = UserRepository()
    status_repository = StatusRepository()
    organizer_type_repository = OrganizerTypeRepository()
    faculty_repository = FacultyRepository()

    active_status = status_repository.get_instance_by_name("Activ")

    fiesc = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Electrica si Stiinta Calculatoarelor"
    )
    fdsa = faculty_repository.get_instance_by_name(
        "Facultatea de Drept si Stiinte Administrative"
    )
    feea = faculty_repository.get_instance_by_name(
        "Facultatea de Economie, Administratie si Afaceri"
    )
    fefs = faculty_repository.get_instance_by_name(
        "Facultatea de Educatie Fizica si Sport"
    )
    fia = faculty_repository.get_instance_by_name("Facultatea de Inginerie Alimentara")
    fimar = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Mecanica, Autovehicule si Robotica"
    )
    figs = faculty_repository.get_instance_by_name(
        "Facultatea de Istorie, Geografie si Stiinte Sociale"
    )
    flsc = faculty_repository.get_instance_by_name(
        "Facultatea de Litere si Stiinte ale Comunicarii"
    )
    fmsb = faculty_repository.get_instance_by_name(
        "Facultatea de Medicina si Stiinte Biologice"
    )
    fpse = faculty_repository.get_instance_by_name(
        "Facultatea de Psihologie si Stiinte ale Educatiei"
    )
    fs = faculty_repository.get_instance_by_name("Facultatea de Silvicultura")

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
        {
            "name": "FIRESC",
            "description": "Asociatia studenteasca FIRESC din cadrul FIESC, implicata in evenimente, workshop-uri si activitati pentru studenti.",
            "link": "https://www.facebook.com/firesc",
            "organizer_type": student_association,
            "user": user_repository.get_instance_by_username("organization_firesc"),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "ASUS",
            "description": "Asociatia Studentilor din Universitatea Suceava, implicata in reprezentarea studentilor si organizarea de activitati studentesti.",
            "link": "https://www.facebook.com/ASUS.Suceava",
            "organizer_type": student_association,
            "user": user_repository.get_instance_by_username("organization_asus"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "AIESEC Suceava",
            "description": "Organizatie studenteasca internationala prezenta in mediul universitar, orientata spre leadership, voluntariat si proiecte pentru tineri.",
            "link": "https://aiesec.org",
            "organizer_type": student_association,
            "user": user_repository.get_instance_by_username("organization_aiesec"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "ANSSA",
            "description": "Asociatia Nationala a Studentilor in Stiinte Administrative, implicata in activitati academice si studentesti.",
            "link": "https://www.facebook.com",
            "organizer_type": student_association,
            "user": user_repository.get_instance_by_username("organization_anssa"),
            "status": active_status,
            "faculty": fdsa,
        },
        {
            "name": "ASCOR Suceava",
            "description": "Asociatia Studentilor Crestini Ortodocsi Romani, filiala Suceava, implicata in activitati culturale, spirituale si de voluntariat.",
            "link": "https://www.facebook.com",
            "organizer_type": student_association,
            "user": user_repository.get_instance_by_username("organization_ascor"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Ansamblul Studentesc Arcanul",
            "description": "Ansamblu studentesc al USV dedicat activitatilor culturale, artistice si promovarii traditiilor romanesti.",
            "link": "https://www.facebook.com",
            "organizer_type": university_club,
            "user": user_repository.get_instance_by_username("organization_arcanul"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Asociatia de Arta Nicolae Tonitza",
            "description": "Organizatie studenteasca orientata spre arta, cultura si activitati creative.",
            "link": "https://www.facebook.com",
            "organizer_type": university_club,
            "user": user_repository.get_instance_by_username("organization_tonitza"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Teatrul Studentesc Fabulinus",
            "description": "Trupa de teatru studentesc a USV, implicata in spectacole, evenimente culturale si activitati artistice.",
            "link": "https://www.facebook.com/fabulinus",
            "organizer_type": university_club,
            "user": user_repository.get_instance_by_username("organization_fabulinus"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Casa de Cultura a Studentilor USV",
            "description": "Structura culturala care organizeaza evenimente artistice, spectacole si activitati pentru studenti.",
            "link": "https://usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_ccs_usv"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Biblioteca USV",
            "description": "Biblioteca Universitatii Stefan cel Mare din Suceava, organizatoare de simpozioane, lansari de carte si evenimente culturale.",
            "link": "https://biblioteca.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username(
                "organization_biblioteca_usv"
            ),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Centrul de Consiliere si Orientare in Cariera USV",
            "description": "Centrul USV dedicat consilierii studentilor, orientarii in cariera, workshop-urilor si intalnirilor cu angajatori.",
            "link": "https://usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_ccoc_usv"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Radio USV",
            "description": "Structura media universitara implicata in promovarea evenimentelor, proiectelor si activitatilor studentesti.",
            "link": "https://radio.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_radio_usv"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Departamentul de Calculatoare FIESC",
            "description": "Departament academic din cadrul FIESC, implicat in evenimente tehnice, conferinte, prezentari si activitati pentru studenti.",
            "link": "https://fiesc.usv.ro/departamentul-de-calculatoare/",
            "organizer_type": professor,
            "user": user_repository.get_instance_by_username(
                "organization_dep_calculatoare"
            ),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "Departamentul de Electrotehnica FIESC",
            "description": "Departament academic din cadrul FIESC, implicat in activitati de cercetare, prezentari tehnice si evenimente studentesti.",
            "link": "https://fiesc.usv.ro",
            "organizer_type": professor,
            "user": user_repository.get_instance_by_username(
                "organization_dep_electrotehnica"
            ),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "Facultatea de Inginerie Electrica si Stiinta Calculatoarelor",
            "description": "Facultate USV care organizeaza conferinte, workshop-uri, concursuri studentesti si evenimente tehnice.",
            "link": "https://fiesc.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_fiesc"),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "Facultatea de Economie, Administratie si Afaceri",
            "description": "Facultate USV care organizeaza conferinte, dezbateri, workshop-uri si evenimente academice din domeniul economic.",
            "link": "https://feaa.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_feea"),
            "status": active_status,
            "faculty": feea,
        },
        {
            "name": "Facultatea de Drept si Stiinte Administrative",
            "description": "Facultate USV care organizeaza conferinte, dezbateri si evenimente academice in domeniul juridic si administrativ.",
            "link": "https://fdsa.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_fdsa"),
            "status": active_status,
            "faculty": fdsa,
        },
        {
            "name": "Facultatea de Litere si Stiinte ale Comunicarii",
            "description": "Facultate USV implicata in evenimente culturale, conferinte, sesiuni stiintifice si proiecte de comunicare.",
            "link": "https://flsc.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_flsc"),
            "status": active_status,
            "faculty": flsc,
        },
        {
            "name": "Facultatea de Psihologie si Stiinte ale Educatiei",
            "description": "Facultate USV care organizeaza workshop-uri, conferinte si activitati educationale si psihologice.",
            "link": "https://fpse.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_fpse"),
            "status": active_status,
            "faculty": fpse,
        },
        {
            "name": "Facultatea de Silvicultura",
            "description": "Facultate USV implicata in evenimente stiintifice, activitati de cercetare si proiecte dedicate mediului si silviculturii.",
            "link": "https://silvic.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username(
                "organization_silvicultura"
            ),
            "status": active_status,
            "faculty": fs,
        },
        {
            "name": "Facultatea de Inginerie Alimentara",
            "description": "Facultate USV care organizeaza evenimente academice, workshop-uri si activitati aplicate in domeniul alimentar.",
            "link": "https://fia.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_fia"),
            "status": active_status,
            "faculty": fia,
        },
        {
            "name": "Facultatea de Inginerie Mecanica, Autovehicule si Robotica",
            "description": "Facultate USV orientata spre evenimente tehnice, demonstratii, workshop-uri si activitati aplicate in inginerie.",
            "link": "https://fimar.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_fimar"),
            "status": active_status,
            "faculty": fimar,
        },
        {
            "name": "Facultatea de Educatie Fizica si Sport",
            "description": "Facultate USV implicata in competitii, activitati sportive, workshop-uri si proiecte pentru sanatate si miscare.",
            "link": "https://fefs.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_fefs"),
            "status": active_status,
            "faculty": fefs,
        },
        {
            "name": "Facultatea de Istorie, Geografie si Stiinte Sociale",
            "description": "Facultate USV care organizeaza conferinte, dezbateri si activitati academice in domeniul istoriei, geografiei si stiintelor sociale.",
            "link": "https://figs.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_figs"),
            "status": active_status,
            "faculty": figs,
        },
        {
            "name": "Facultatea de Medicina si Stiinte Biologice",
            "description": "Facultate USV implicata in conferinte, seminare si activitati academice in domeniul medical si biologic.",
            "link": "https://fmsb.usv.ro",
            "organizer_type": university_structure,
            "user": user_repository.get_instance_by_username("organization_fmsb"),
            "status": active_status,
            "faculty": fmsb,
        },
        {
            "name": "ASSIST Software",
            "description": "Companie IT din Suceava, partener educational si organizator de evenimente, internship-uri si workshop-uri pentru studenti.",
            "link": "https://assist-software.net",
            "organizer_type": external_partner,
            "user": user_repository.get_instance_by_username("organization_assist"),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "OSF Digital",
            "description": "Companie IT mentionata in ecosistemul FIESC, implicata in colaborari educationale si activitati pentru studenti.",
            "link": "https://osf.digital",
            "organizer_type": external_partner,
            "user": user_repository.get_instance_by_username("organization_osf"),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "Silicon Service",
            "description": "Companie partenera mentionata in ecosistemul FIESC, relevanta pentru activitati tehnice si colaborari cu studenti.",
            "link": "https://www.siliconservice.ro",
            "organizer_type": external_partner,
            "user": user_repository.get_instance_by_username(
                "organization_silicon_service"
            ),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "Volter",
            "description": "Companie mentionata in anunturi FIESC pentru stagii de practica si internship-uri.",
            "link": "https://www.volter.ro",
            "organizer_type": external_partner,
            "user": user_repository.get_instance_by_username("organization_volter"),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "C&A Connect",
            "description": "Companie mentionata in anunturi FIESC pentru stagii de practica, potrivita pentru evenimente de cariera si internship.",
            "link": "https://www.facebook.com",
            "organizer_type": external_partner,
            "user": user_repository.get_instance_by_username("organization_ca_connect"),
            "status": active_status,
            "faculty": fiesc,
        },
        {
            "name": "Fundația Schuman Romania",
            "description": "Organizatie partenera in evenimente gazduite de USV, inclusiv conferinte cu tematica europeana.",
            "link": "https://www.schuman.ro",
            "organizer_type": external_partner,
            "user": user_repository.get_instance_by_username("organization_schuman"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Consiliul Judetean Suceava",
            "description": "Institutie publica locala care poate colabora cu USV in proiecte, conferinte si evenimente regionale.",
            "link": "https://www.cjsuceava.ro",
            "organizer_type": public_institution,
            "user": user_repository.get_instance_by_username("organization_cj_suceava"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Primaria Municipiului Suceava",
            "description": "Institutie publica locala implicata in activitati comunitare, culturale si educationale din municipiul Suceava.",
            "link": "https://www.primariasv.ro",
            "organizer_type": public_institution,
            "user": user_repository.get_instance_by_username(
                "organization_primaria_suceava"
            ),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Teatrul pentru Copii si Tineret Vasilache",
            "description": "Institutie culturala invitata in evenimente si spectacole gazduite de USV.",
            "link": "https://www.teatrulvasilache.ro",
            "organizer_type": external_partner,
            "user": user_repository.get_instance_by_username(
                "organization_teatrul_vasilache"
            ),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "Evoluat",
            "description": "Agentie implicata in organizarea de evenimente de branding si antreprenoriat gazduite la USV.",
            "link": "https://www.evoluat.ro",
            "organizer_type": external_partner,
            "user": user_repository.get_instance_by_username("organization_evoluat"),
            "status": active_status,
            "faculty": None,
        },
        {
            "name": "USV Computer Science Department",
            "description": "Academic department that organizes conferences and technical presentations.",
            "link": "https://usv.ro",
            "organizer_type": organizer_type_repository.get_instance_by_name(
                "Profesor"
            ),
            "user": user_repository.get_instance_by_username("professor"),
            "status": active_status,
            "faculty": fiesc,
        },
    ]
