def default_user_data():
    """
    Returnează utilizatorii default utilizați
    pentru popularea inițială a bazei de date.

    Utilizatorii includ:
    - administratori,
    - studenți,
    - profesori,
    - organizații,
    - parteneri,
    - structuri universitare.
    """

    return [
        # =====================================================
        # DEFAULT SYSTEM USERS
        # =====================================================
        {
            "username": "administrator",
            "password": "Admin#1",
            "email": "admin@usv.ro",
            "first_name": "System",
            "last_name": "Administrator",
            "is_staff": True,
            "is_superuser": True,
        },
        {
            "username": "student",
            "password": "Student#1",
            "email": "student@student.usv.ro",
            "first_name": "Default",
            "last_name": "Student",
        },
        {
            "username": "professor",
            "password": "Professor#1",
            "email": "professor@usv.ro",
            "first_name": "Default",
            "last_name": "Professor",
        },
        {
            "username": "partner",
            "password": "Partner#1",
            "email": "partner@example.com",
            "first_name": "Default",
            "last_name": "Partner",
        },
        {
            "username": "organization",
            "password": "Organization#1",
            "email": "organization@example.com",
            "first_name": "Default",
            "last_name": "Organization",
        },
        {
            "username": "guest",
            "password": "Guest#1",
            "email": "guest@example.com",
            "first_name": "Default",
            "last_name": "Guest",
        },
        # =====================================================
        # STUDENT ORGANIZATIONS
        # =====================================================
        {
            "username": "organization_firesc",
            "password": "Organization#1",
            "email": "firesc@usv.ro",
            "first_name": "FIRESC",
            "last_name": "Organization",
        },
        {
            "username": "organization_asus",
            "password": "Organization#1",
            "email": "asus@usv.ro",
            "first_name": "ASUS",
            "last_name": "Organization",
        },
        {
            "username": "organization_aiesec",
            "password": "Organization#1",
            "email": "aiesec@usv.ro",
            "first_name": "AIESEC",
            "last_name": "Organization",
        },
        {
            "username": "organization_anssa",
            "password": "Organization#1",
            "email": "anssa@usv.ro",
            "first_name": "ANSSA",
            "last_name": "Organization",
        },
        {
            "username": "organization_ascor",
            "password": "Organization#1",
            "email": "ascor@usv.ro",
            "first_name": "ASCOR",
            "last_name": "Organization",
        },
        {
            "username": "organization_arcanul",
            "password": "Organization#1",
            "email": "arcanul@usv.ro",
            "first_name": "Arcanul",
            "last_name": "Organization",
        },
        # =====================================================
        # USV STRUCTURES
        # =====================================================
        {
            "username": "organization_fiesc",
            "password": "Organization#1",
            "email": "fiesc@usv.ro",
            "first_name": "FIESC",
            "last_name": "USV",
        },
        {
            "username": "organization_feea",
            "password": "Organization#1",
            "email": "feaa@usv.ro",
            "first_name": "FEAA",
            "last_name": "USV",
        },
        {
            "username": "organization_fdsa",
            "password": "Organization#1",
            "email": "fdsa@usv.ro",
            "first_name": "FDSA",
            "last_name": "USV",
        },
        {
            "username": "organization_flsc",
            "password": "Organization#1",
            "email": "flsc@usv.ro",
            "first_name": "FLSC",
            "last_name": "USV",
        },
        {
            "username": "organization_fpse",
            "password": "Organization#1",
            "email": "fpse@usv.ro",
            "first_name": "FPSE",
            "last_name": "USV",
        },
        # =====================================================
        # EXTERNAL PARTNERS
        # =====================================================
        {
            "username": "organization_assist",
            "password": "Organization#1",
            "email": "assist@assist-software.net",
            "first_name": "ASSIST",
            "last_name": "Software",
        },
        {
            "username": "organization_osf",
            "password": "Organization#1",
            "email": "contact@osf.digital",
            "first_name": "OSF",
            "last_name": "Digital",
        },
        {
            "username": "organization_silicon_service",
            "password": "Organization#1",
            "email": "contact@siliconservice.ro",
            "first_name": "Silicon",
            "last_name": "Service",
        },
        {
            "username": "organization_cj_suceava",
            "password": "Organization#1",
            "email": "contact@cjsuceava.ro",
            "first_name": "Consiliul",
            "last_name": "Judetean",
        },
        {
            "username": "organization_primaria_suceava",
            "password": "Organization#1",
            "email": "primaria@primariasv.ro",
            "first_name": "Primaria",
            "last_name": "Suceava",
        },
    ]
