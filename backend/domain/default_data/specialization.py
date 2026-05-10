from api.repository import FacultyRepository


def default_specialization_data():
    faculty_repository = FacultyRepository()

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
        # Facultatea de Drept si Stiinte Administrative - licenta
        {"name": "Drept", "faculty": fdsa},
        {"name": "Drept european si international", "faculty": fdsa},
        {"name": "Administratie publica", "faculty": fdsa},
        {"name": "Politie locala", "faculty": fdsa},
        {"name": "Asistenta manageriala si administrativa", "faculty": fdsa},
        # Facultatea de Drept si Stiinte Administrative - master
        {"name": "Drept european", "faculty": fdsa},
        {"name": "Drept penal si criminalistica", "faculty": fdsa},
        {"name": "Management si administratie europeana", "faculty": fdsa},
        {"name": "Management si audit in administratie si afaceri", "faculty": fdsa},
        # Facultatea de Economie, Administratie si Afaceri - licenta
        {"name": "Matematica informatica", "faculty": feaa},
        {"name": "Economia comertului, turismului si serviciilor", "faculty": feaa},
        {"name": "Administrarea afacerilor", "faculty": feaa},
        {"name": "Informatica economica", "faculty": feaa},
        {"name": "Contabilitate si informatica de gestiune", "faculty": feaa},
        {"name": "Economie generala si comunicare economica", "faculty": feaa},
        {"name": "Afaceri internationale", "faculty": feaa},
        {"name": "Finante si banci", "faculty": feaa},
        {"name": "Management", "faculty": feaa},
        # Facultatea de Economie, Administratie si Afaceri - master
        {
            "name": "Administrarea si formarea resurselor umane in organizatii",
            "faculty": feaa,
        },
        {"name": "Management si administrarea afacerilor", "faculty": feaa},
        {
            "name": "Managementul firmelor de comert, turism si servicii",
            "faculty": feaa,
        },
        {
            "name": "Planificarea noilor produse turistice si managementul destinatiei",
            "faculty": feaa,
        },
        {
            "name": "Contabilitate, audit financiar si expertiza contabila",
            "faculty": feaa,
        },
        {"name": "Audit si guvernanta corporativa", "faculty": feaa},
        {"name": "Globalizare si diplomatie economica", "faculty": feaa},
        {"name": "Economie si afaceri internationale", "faculty": feaa},
        {"name": "Digitalizare si data science", "faculty": feaa},
        # Facultatea de Educatie Fizica si Sport - licenta
        {"name": "Educatie fizica si sportiva", "faculty": fefs},
        {"name": "Kinetoterapie si motricitate speciala", "faculty": fefs},
        # Facultatea de Educatie Fizica si Sport - master
        {
            "name": "Educatie fizica scolara si activitati extracurriculare",
            "faculty": fefs,
        },
        {
            "name": "Kinetoprofilaxie, recuperare si remodelare corporala",
            "faculty": fefs,
        },
        # Facultatea de Inginerie Alimentara - licenta
        {"name": "Controlul si expertiza produselor alimentare", "faculty": fia},
        {"name": "Ingineria produselor alimentare", "faculty": fia},
        {"name": "Protectia consumatorului si a mediului", "faculty": fia},
        {
            "name": "Inginerie si management in alimentatia publica si agroturism",
            "faculty": fia,
        },
        {"name": "Stiinte gastronomice", "faculty": fia},
        # Facultatea de Inginerie Alimentara - master
        {
            "name": "Managementul igienei, controlul calitatii produselor alimentare si asigurarea sanatatii populatiei",
            "faculty": fia,
        },
        {
            "name": "Managementul securitatii mediului si siguranta alimentara",
            "faculty": fia,
        },
        {
            "name": "Managementul suplimentelor alimentare si al produselor pentru sanatate",
            "faculty": fia,
        },
        # Facultatea de Inginerie Electrica si Stiinta Calculatoarelor - licenta
        {"name": "Calculatoare", "faculty": fiesc},
        {"name": "Calculatoare - invatamant dual", "faculty": fiesc},
        {"name": "Automatica si informatica aplicata", "faculty": fiesc},
        {
            "name": "Automatica si informatica aplicata - invatamant dual",
            "faculty": fiesc,
        },
        {"name": "Sisteme electrice", "faculty": fiesc},
        {"name": "Sisteme electrice - invatamant dual", "faculty": fiesc},
        {"name": "Electronica aplicata", "faculty": fiesc},
        {"name": "Retele si software de telecomunicatii", "faculty": fiesc},
        {"name": "Managementul energiei", "faculty": fiesc},
        {"name": "Energetica si tehnologii informatice", "faculty": fiesc},
        {
            "name": "Echipamente si sisteme de comanda si control pentru autovehicule",
            "faculty": fiesc,
        },
        {"name": "Echipamente si sisteme medicale", "faculty": fiesc},
        # Facultatea de Inginerie Electrica si Stiinta Calculatoarelor - master
        {"name": "Tehnici avansate in masini si actionari electrice", "faculty": fiesc},
        {
            "name": "Sisteme moderne pentru conducerea proceselor energetice",
            "faculty": fiesc,
        },
        {"name": "Retele de comunicatii si calculatoare", "faculty": fiesc},
        {"name": "Securitate cibernetica", "faculty": fiesc},
        {"name": "Stiinta si ingineria calculatoarelor", "faculty": fiesc},
        # Facultatea de Inginerie Mecanica, Autovehicule si Robotica - licenta
        {"name": "Tehnologia constructiilor de masini", "faculty": fimar},
        {
            "name": "Tehnologia constructiilor de masini - invatamant dual",
            "faculty": fimar,
        },
        {"name": "Inginerie mecanica", "faculty": fimar},
        {"name": "Inginerie mecanica - invatamant dual", "faculty": fimar},
        {"name": "Mecatronica", "faculty": fimar},
        {"name": "Robotica", "faculty": fimar},
        {"name": "Autovehicule rutiere", "faculty": fimar},
        # Facultatea de Inginerie Mecanica, Autovehicule si Robotica - master
        {
            "name": "Expertiza tehnica, evaluare economica si management",
            "faculty": fimar,
        },
        {"name": "Mecatronica aplicata", "faculty": fimar},
        {"name": "Mecatronica autovehiculelor", "faculty": fimar},
        {
            "name": "Ingineria si managementul calitatii, sanatatii si securitatii in munca",
            "faculty": fimar,
        },
        # Facultatea de Istorie, Geografie si Stiinte Sociale - licenta
        {"name": "Asistenta sociala", "faculty": fig},
        {"name": "Filosofie", "faculty": fig},
        {"name": "Geografia turismului", "faculty": fig},
        {"name": "Geografie", "faculty": fig},
        {"name": "Istorie", "faculty": fig},
        {"name": "Relatii internationale si studii europene", "faculty": fig},
        {"name": "Resurse umane", "faculty": fig},
        # Facultatea de Istorie, Geografie si Stiinte Sociale - master
        {
            "name": "Managementul relatiilor internationale si cooperarii transfrontaliere",
            "faculty": fig,
        },
        {"name": "Istorie: permanente, interferente si schimbare", "faculty": fig},
        {"name": "Turism si dezvoltare regionala", "faculty": fig},
        {"name": "GIS si planificare teritoriala", "faculty": fig},
        {"name": "Etica aplicata si auditul eticii in organizatii", "faculty": fig},
        {
            "name": "Managementul serviciilor sociale si de securitate comunitara",
            "faculty": fig,
        },
        # Facultatea de Litere si Stiinte ale Comunicarii - licenta
        {
            "name": "Limba si literatura engleza - Limba si literatura germana / Limba si literatura romana",
            "faculty": flsc,
        },
        {
            "name": "Limba si literatura engleza - Limba si literatura moderna",
            "faculty": flsc,
        },
        {
            "name": "Limba si literatura franceza - Limba si literatura moderna",
            "faculty": flsc,
        },
        {
            "name": "Limba si literatura romana - O limba si literatura moderna",
            "faculty": flsc,
        },
        {
            "name": "Limba si literatura ucraineana - O limba si literatura moderna / Limba si literatura romana",
            "faculty": flsc,
        },
        {"name": "Comunicare si relatii publice", "faculty": flsc},
        {"name": "Media digitala", "faculty": flsc},
        {"name": "Cinematografie, fotografie, media", "faculty": flsc},
        # Facultatea de Litere si Stiinte ale Comunicarii - master
        {
            "name": "Cultura si civilizatie britanica in contextul globalizarii",
            "faculty": flsc,
        },
        {"name": "Limba si comunicare", "faculty": flsc},
        {"name": "Literatura romana in context european", "faculty": flsc},
        {"name": "Teoria si practica traducerii", "faculty": flsc},
        {"name": "Engleza in era digitala", "faculty": flsc},
        {"name": "Comunicare, media si industriile creative", "faculty": flsc},
        # Facultatea de Medicina si Stiinte Biologice - licenta
        {"name": "Medicina", "faculty": fmsb},
        {"name": "Asistenta medicala generala", "faculty": fmsb},
        {"name": "Balneofiziokinetoterapie si recuperare", "faculty": fmsb},
        {"name": "Nutritie si dietetica", "faculty": fmsb},
        {"name": "Tehnica dentara", "faculty": fmsb},
        {"name": "Biologie", "faculty": fmsb},
        {"name": "Biochimie", "faculty": fmsb},
        # Facultatea de Medicina si Stiinte Biologice - master
        {"name": "Nutritie si recuperare medicala", "faculty": fmsb},
        # Facultatea de Silvicultura - licenta
        {"name": "Silvicultura", "faculty": fs},
        {"name": "Ecologie si protectia mediului", "faculty": fs},
        # Facultatea de Silvicultura - master
        {
            "name": "Conservarea biodiversitatii si managementul ecosistemelor",
            "faculty": fs,
        },
        {"name": "Managementul activitatilor din domeniul forestier", "faculty": fs},
        # Facultatea de Psihologie si Stiinte ale Educatiei - licenta
        {"name": "Pedagogia invatamantului primar si prescolar", "faculty": fsed},
        {"name": "Psihologie", "faculty": fsed},
        # Facultatea de Psihologie si Stiinte ale Educatiei - master
        {"name": "Managementul institutiilor educationale", "faculty": fsed},
        {"name": "Consiliere scolara si educatie emotionala", "faculty": fsed},
        {"name": "Rezilienta in educatie", "faculty": fsed},
        {"name": "Comunicare didactica", "faculty": fsed},
    ]
