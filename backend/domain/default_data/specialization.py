from api.repository import FacultyRepository


def default_specialization_data():
    """
    Returnează lista specializărilor default
    utilizate pentru popularea inițială a bazei de date.

    Specializările sunt asociate facultăților
    și includ programe de:
    - licență,
    - master.
    """

    # =====================================================
    # REPOSITORY
    # =====================================================

    faculty_repository = FacultyRepository()

    # =====================================================
    # FACULTATI
    # =====================================================

    fdsa = faculty_repository.get_instance_by_name(
        "Facultatea de Drept si Stiinte Administrative"
    )

    feaa = faculty_repository.get_instance_by_name(
        "Facultatea de Economie, Administratie si Afaceri"
    )

    fefs = faculty_repository.get_instance_by_name(
        "Facultatea de Educatie Fizica si Sport"
    )

    fia = faculty_repository.get_instance_by_name("Facultatea de Inginerie Alimentara")

    fiesc = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Electrica si Stiinta Calculatoarelor"
    )

    fimar = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Mecanica, Autovehicule si Robotica"
    )

    fig = faculty_repository.get_instance_by_name(
        "Facultatea de Istorie, Geografie si Stiinte Sociale"
    )

    flsc = faculty_repository.get_instance_by_name(
        "Facultatea de Litere si Stiinte ale Comunicarii"
    )

    fmsb = faculty_repository.get_instance_by_name(
        "Facultatea de Medicina si Stiinte Biologice"
    )

    fsed = faculty_repository.get_instance_by_name(
        "Facultatea de Psihologie si Stiinte ale Educatiei"
    )

    fs = faculty_repository.get_instance_by_name("Facultatea de Silvicultura")

    return [
        # =====================================================
        # FDSA - LICENTA
        # =====================================================
        {"name": "Drept", "faculty": fdsa},
        {
            "name": "Drept european si international",
            "faculty": fdsa,
        },
        {
            "name": "Administratie publica",
            "faculty": fdsa,
        },
        {
            "name": "Politie locala",
            "faculty": fdsa,
        },
        {
            "name": ("Asistenta manageriala si administrativa"),
            "faculty": fdsa,
        },
        # =====================================================
        # FDSA - MASTER
        # =====================================================
        {
            "name": "Drept european",
            "faculty": fdsa,
        },
        {
            "name": "Drept penal si criminalistica",
            "faculty": fdsa,
        },
        {
            "name": ("Management si administratie europeana"),
            "faculty": fdsa,
        },
        {
            "name": ("Management si audit in administratie " "si afaceri"),
            "faculty": fdsa,
        },
        # =====================================================
        # FEAA - LICENTA
        # =====================================================
        {
            "name": "Matematica informatica",
            "faculty": feaa,
        },
        {
            "name": ("Economia comertului, turismului " "si serviciilor"),
            "faculty": feaa,
        },
        {
            "name": "Administrarea afacerilor",
            "faculty": feaa,
        },
        {
            "name": "Informatica economica",
            "faculty": feaa,
        },
        {
            "name": ("Contabilitate si informatica " "de gestiune"),
            "faculty": feaa,
        },
        {
            "name": ("Economie generala si comunicare " "economica"),
            "faculty": feaa,
        },
        {
            "name": "Afaceri internationale",
            "faculty": feaa,
        },
        {
            "name": "Finante si banci",
            "faculty": feaa,
        },
        {
            "name": "Management",
            "faculty": feaa,
        },
        # =====================================================
        # FEAA - MASTER
        # =====================================================
        {
            "name": ("Administrarea si formarea " "resurselor umane in organizatii"),
            "faculty": feaa,
        },
        {
            "name": ("Management si administrarea afacerilor"),
            "faculty": feaa,
        },
        {
            "name": ("Managementul firmelor de comert, " "turism si servicii"),
            "faculty": feaa,
        },
        {
            "name": (
                "Planificarea noilor produse turistice " "si managementul destinatiei"
            ),
            "faculty": feaa,
        },
        {
            "name": ("Contabilitate, audit financiar " "si expertiza contabila"),
            "faculty": feaa,
        },
        {
            "name": ("Audit si guvernanta corporativa"),
            "faculty": feaa,
        },
        {
            "name": ("Globalizare si diplomatie economica"),
            "faculty": feaa,
        },
        {
            "name": ("Economie si afaceri internationale"),
            "faculty": feaa,
        },
        {
            "name": ("Digitalizare si data science"),
            "faculty": feaa,
        },
        # =====================================================
        # FIESC - LICENTA
        # =====================================================
        {
            "name": "Calculatoare",
            "faculty": fiesc,
        },
        {
            "name": ("Calculatoare - invatamant dual"),
            "faculty": fiesc,
        },
        {
            "name": ("Automatica si informatica aplicata"),
            "faculty": fiesc,
        },
        {
            "name": ("Automatica si informatica aplicata " "- invatamant dual"),
            "faculty": fiesc,
        },
        {
            "name": "Sisteme electrice",
            "faculty": fiesc,
        },
        {
            "name": ("Electronica aplicata"),
            "faculty": fiesc,
        },
        {
            "name": ("Retele si software " "de telecomunicatii"),
            "faculty": fiesc,
        },
        {
            "name": ("Managementul energiei"),
            "faculty": fiesc,
        },
        {
            "name": ("Energetica si tehnologii informatice"),
            "faculty": fiesc,
        },
        {
            "name": ("Echipamente si sisteme medicale"),
            "faculty": fiesc,
        },
        # =====================================================
        # FIESC - MASTER
        # =====================================================
        {
            "name": ("Tehnici avansate in masini " "si actionari electrice"),
            "faculty": fiesc,
        },
        {
            "name": ("Sisteme moderne pentru conducerea " "proceselor energetice"),
            "faculty": fiesc,
        },
        {
            "name": ("Retele de comunicatii si calculatoare"),
            "faculty": fiesc,
        },
        {
            "name": "Securitate cibernetica",
            "faculty": fiesc,
        },
        {
            "name": ("Stiinta si ingineria calculatoarelor"),
            "faculty": fiesc,
        },
        # =====================================================
        # MEDICINA
        # =====================================================
        {
            "name": "Medicina",
            "faculty": fmsb,
        },
        {
            "name": ("Asistenta medicala generala"),
            "faculty": fmsb,
        },
        {
            "name": ("Balneofiziokinetoterapie " "si recuperare"),
            "faculty": fmsb,
        },
        {
            "name": ("Nutritie si dietetica"),
            "faculty": fmsb,
        },
        {
            "name": "Biologie",
            "faculty": fmsb,
        },
        {
            "name": "Biochimie",
            "faculty": fmsb,
        },
        # =====================================================
        # PSIHOLOGIE
        # =====================================================
        {
            "name": ("Pedagogia invatamantului primar " "si prescolar"),
            "faculty": fsed,
        },
        {
            "name": "Psihologie",
            "faculty": fsed,
        },
        {
            "name": ("Managementul institutiilor " "educationale"),
            "faculty": fsed,
        },
        {
            "name": ("Consiliere scolara " "si educatie emotionala"),
            "faculty": fsed,
        },
        # =====================================================
        # SILVICULTURA
        # =====================================================
        {
            "name": "Silvicultura",
            "faculty": fs,
        },
        {
            "name": ("Ecologie si protectia mediului"),
            "faculty": fs,
        },
    ]
