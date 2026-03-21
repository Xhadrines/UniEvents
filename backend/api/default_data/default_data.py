from django.utils import timezone
from datetime import datetime

from ..repository import (
    FacultateRepository,
    SpecializareRepository,
    RolRepository,
    StareRepository,
    UserRepository,
    TipRepository,
    OrganizatorRepository,
    LocatieRepository,
    CategorieRepository,
    TipParticipareRepository,
    SponsorRepository,
    EvenimentRepository,
)


def default_user_data():
    return [
        {
            "username": "administrator",
            "password": "Admin#1",
            "email": "admin@exemplu.com",
            "first_name": "Administrator",
            "last_name": "Examplu",
        },
        {
            "username": "student",
            "password": "Student#1",
            "email": "student@exemplu.com",
            "first_name": "Student",
            "last_name": "Examplu",
        },
        {
            "username": "profesor",
            "password": "Profesor#1",
            "email": "profesor@exemplu.com",
            "first_name": "Profesor",
            "last_name": "Examplu",
        },
        {
            "username": "partener",
            "password": "Partener#1",
            "email": "partener@exemplu.com",
            "first_name": "Partener",
            "last_name": "Examplu",
        },
        {
            "username": "organizatie",
            "password": "Organizatie#1",
            "email": "organizatie@exemplu.com",
            "first_name": "Organizatie",
            "last_name": "Examplu",
        },
    ]


def default_faultate_data():
    return [
        {
            "nume": "Facultatea de Drept si Stiinte Administrative",
        },
        {
            "nume": "Facultatea de Economie, Administratie si Afaceri",
        },
        {
            "nume": "Facultatea de Educatie Fizica si Sport",
        },
        {
            "nume": "Facultatea de Inginerie Alimentara",
        },
        {
            "nume": "Facultatea de Inginerie Electrica și Stiinta Calculatoarelor",
        },
        {
            "nume": "Facultatea de Inginerie Mecanica, Autovehicule si Robotica",
        },
        {
            "nume": "Facultatea de Istorie, Geografie si Stiinte Sociale",
        },
        {
            "nume": "Facultatea de Litere si Stiinte ale Comunicarii",
        },
        {
            "nume": "Facultatea de Medicina si Stiinte Biologice",
        },
        {
            "nume": "Facultatea de Psihologie si Stiinte ale Educatiei",
        },
        {
            "nume": "Facultatea de Silvicultura",
        },
    ]


def default_specializari_data():
    facultate = FacultateRepository()

    facultate_id = facultate.get_instance_by_name(
        "Facultatea de Inginerie Electrica și Stiinta Calculatoarelor"
    )

    return [
        {
            "nume": "Calculatoare",
            "facultate": facultate_id,
        },
        {
            "nume": "Electronica aplicata",
            "facultate": facultate_id,
        },
        {
            "nume": "Retele si software de telecomunicatii",
            "facultate": facultate_id,
        },
        {
            "nume": "Sisteme electrice",
            "facultate": facultate_id,
        },
        {
            "nume": "Energetica si tehnologii informatice",
            "facultate": facultate_id,
        },
        {
            "nume": "Managementul energiei",
            "facultate": facultate_id,
        },
        {
            "nume": "Automatica si informatica aplicata",
            "facultate": facultate_id,
        },
        {
            "nume": "Echipamente si sisteme de comanda si control pentru autovehicule",
            "facultate": facultate_id,
        },
        {
            "nume": "Echipamente si sisteme medicale",
            "facultate": facultate_id,
        },
    ]


def default_rol_data():
    return [
        {
            "nume": "Administrator",
            "descriere": "Rol cu privilegii complete asupra sistemului, responsabil pentru gestionarea utilizatorilor, evenimentelor si altor aspecte administrative.",
        },
        {
            "nume": "Student",
            "descriere": "Rol pentru utilizatorii care participa la cursuri si activitati academice.",
        },
        {
            "nume": "Profesor",
            "descriere": "Rol pentru utilizatorii care predau cursuri si conduc activitati academice.",
        },
        {
            "nume": "Partener",
            "descriere": "Rol pentru utilizatorii care colaboreaza cu institutia in diverse proiecte, evenimente sau activitati, dar care nu sunt implicati direct in procesul educational sau administrativ al institutiei.",
        },
        {
            "nume": "Organizatie",
            "descriere": "Rol pentru entitati juridice sau organizatii care interactioneaza cu platforma in scopul organizarii de evenimente, colaborarii institutionale sau promovarii de oportunitati pentru studenti si cadre didactice, fara a avea implicare directa in activitatile academice interne.",
        },
        {
            "nume": "Altele",
            "descriere": "Rol pentru utilizatori care nu se încadrează în categoriile standard.",
        },
    ]


def default_stare_data():
    return [
        {
            "nume": "Activ",
            "descriere": "Stare care indica faptul ca un obiect sau o entitate este in prezent activ si functionala.",
        },
        {
            "nume": "Inactiv",
            "descriere": "Stare care indica faptul ca un obiect sau o entitate nu este in prezent activa sau functionala, dar poate fi reactivata in viitor.",
        },
        {
            "nume": "Sters",
            "descriere": "Stare care indica faptul ca un obiect sau o entitate a fost eliminata sau marcata pentru stergere, si nu mai este considerata activa sau functionala in sistem.",
        },
        {
            "nume": "In asteptare",
            "descriere": "Stare care indica faptul ca un obiect sau o entitate este in proces de evaluare, aprobare sau finalizare, si nu este inca considerata activa sau functionala in sistem.",
        },
        {
            "nume": "Anulat",
            "descriere": "Stare care indica faptul ca un obiect sau o entitate a fost anulata sau desfiintata, si nu mai poate fi reactivata.",
        },
        {
            "nume": "Respins",
            "descriere": "Stare care indica faptul ca un obiect sau o entitate a fost respinsa sau refuzata, si nu este considerata activa sau functionala in sistem.",
        },
        {
            "nume": "Acceptat",
            "descriere": "Stare care indica faptul ca un obiect sau o entitate a fost acceptata, si este considerata activa sau functionala in sistem.",
        },
    ]


def default_user_profiles_data():
    facultate = FacultateRepository()
    specializare = SpecializareRepository()
    rol = RolRepository()
    stare = StareRepository()
    user = UserRepository()

    user_id = user.get_instance_by_username("administrator")
    user1_id = user.get_instance_by_username("profesor")
    user2_id = user.get_instance_by_username("student")
    user3_id = user.get_instance_by_username("partener")
    user4_id = user.get_instance_by_username("organizatie")

    facultate_id = facultate.get_instance_by_name(
        "Facultatea de Inginerie Electrica și Stiinta Calculatoarelor"
    )

    specializare_id = specializare.get_instance_by_name("Calculatoare")

    rol_id = rol.get_instance_by_name("Administrator")
    rol1_id = rol.get_instance_by_name("Profesor")
    rol2_id = rol.get_instance_by_name("Student")
    rol3_id = rol.get_instance_by_name("Partener")
    rol4_id = rol.get_instance_by_name("Organizatie")

    stare_id = stare.get_instance_by_name("Activ")

    return [
        {
            "user": user_id,
            "rol": rol_id,
            "stare": stare_id,
        },
        {
            "user": user1_id,
            "rol": rol1_id,
            "stare": stare_id,
        },
        {
            "user": user2_id,
            "facultate": facultate_id,
            "specializare": specializare_id,
            "an_studiu": 1,
            "grupa": 1,
            "semi_grupa": "A",
            "rol": rol2_id,
            "stare": stare_id,
        },
        {
            "user": user3_id,
            "rol": rol3_id,
            "stare": stare_id,
        },
        {
            "user": user4_id,
            "rol": rol4_id,
            "stare": stare_id,
        },
    ]


def default_tip_data():
    return [
        {
            "nume": "Asociatie de studenti",
            "descriere": "Tip de organizator care reprezinta o organizatie formata din studenti, care are ca scop principal promovarea intereselor si nevoilor studentilor, precum si organizarea de activitati si evenimente pentru acestia.",
        },
        {
            "nume": "Conferinta",
            "descriere": "Tip de eveniment care reprezinta o intalnire formala sau informala, unde se prezinta si se discuta subiecte relevante pentru un domeniu specific, adesea cu participarea unor vorbitori invitati sau experti in domeniu.",
        },
        {
            "nume": "Workshop",
            "descriere": "Tip de eveniment care reprezinta o sesiune practica sau interactiva, unde participantii pot invata si aplica abilitati sau cunostinte specifice intr-un mod hands-on.",
        },
        {
            "nume": "Targ de joburi",
            "descriere": "Tip de eveniment care reprezinta o intalnire organizata intre angajatori si potentiali angajati, unde companiile isi prezinta oportunitatile de angajare si participantii pot explora si aplica pentru joburi sau stagii de practica oferite de aceste companii.",
        },
    ]


def default_organizator_data():
    tip = TipRepository()
    user = UserRepository()
    stare = StareRepository()

    tip_id = tip.get_instance_by_name("Asociatie de studenti")

    user_id = user.get_instance_by_username("organizatie")

    stare_id = stare.get_instance_by_name("Activ")

    return [
        {
            "nume": "FIRESC",
            "descriere": "Asociatia de studenti FIRESC (Facultatea de Inginerie Electrica și Stiinta Calculatoarelor) este o organizatie studenteasca dedicata promovarii intereselor si nevoilor studentilor din cadrul facultatii, precum si organizarii de activitati si evenimente pentru acestia. Asociatia FIRESC are ca scop principal crearea unui mediu propice pentru dezvoltarea personala si profesionala a studentilor, prin intermediul unor proiecte, workshop-uri, conferinte si alte activitati care sa raspunda nevoilor si intereselor acestora. Asociatia FIRESC se angajeaza sa ofere oportunitati de invatare, networking si implicare in comunitatea academica, contribuind astfel la formarea unei experiente universitare complete si satisfacatoare pentru toti studentii sai.",
            "link": "https://www.facebook.com/firesc",
            "tip": tip_id,
            "user": user_id,
            "stare": stare_id,
        },
    ]


def default_categorie_data():
    return [
        {
            "nume": "Sport si activitati fizice",
            "descriere": "Categorie care include evenimente sportive, competitii, antrenamente sau activitati recreative menite sa promoveze miscarea, sanatatea si spiritul de echipa.",
        },
        {
            "nume": "Educatie si formare",
            "descriere": "Categorie care cuprinde evenimente educationale precum cursuri, traininguri, seminarii sau sesiuni de formare destinate dezvoltarii cunostintelor si abilitatilor participantilor.",
        },
        {
            "nume": "Tehnologie si IT",
            "descriere": "Categorie dedicata evenimentelor din domeniul tehnologiei informatiei, precum workshop-uri, hackathoane, conferinte sau prezentari legate de software, hardware si inovatie digitala.",
        },
        {
            "nume": "Cultura si arta",
            "descriere": "Categorie care include evenimente culturale precum spectacole, expozitii, proiectii de film, concerte sau alte activitati artistice.",
        },
        {
            "nume": "Cariera si dezvoltare profesionala",
            "descriere": "Categorie care reuneste evenimente orientate spre dezvoltarea profesionala, cum ar fi targuri de joburi, sesiuni de networking, prezentari de companii si workshop-uri de cariera.",
        },
        {
            "nume": "Voluntariat si comunitate",
            "descriere": "Categorie care include activitati de voluntariat, initiative comunitare si evenimente dedicate implicarii sociale si dezvoltarii comunitatii.",
        },
        {
            "nume": "Social si divertisment",
            "descriere": "Categorie destinata evenimentelor recreative si sociale, precum petreceri, intalniri, jocuri sau alte activitati de relaxare si interactiune intre participanti.",
        },
    ]


def default_tip_participare_data():
    return [
        {
            "nume": "Fizic",
            "descriere": "Tip de participare care presupune prezenta fizica a participantilor la locatia desfasurarii evenimentului, oferind interactiune directa si experiente practice.",
        },
        {
            "nume": "Online",
            "descriere": "Tip de participare care permite accesul la eveniment prin intermediul internetului, utilizand platforme digitale pentru vizualizare si interactiune la distanta.",
        },
        {
            "nume": "Hibrid",
            "descriere": "Tip de participare care combina prezenta fizica cu participarea online, oferind flexibilitate participantilor de a alege modul in care doresc sa ia parte la eveniment.",
        },
    ]


def default_locatie_data():
    return [
        {
            "nume": "Aula Magna",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul A",
            "camera": "Aula Magna",
        },
        {
            "nume": "Amfiteatrul A1",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul A",
            "camera": "A1",
        },
        {
            "nume": "Amfiteatrul B1",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul B",
            "camera": "B1",
        },
        {
            "nume": "Laborator Calculatoare 1",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul C",
            "camera": "C201",
        },
        {
            "nume": "Laborator Calculatoare 2",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul C",
            "camera": "C202",
        },
        {
            "nume": "Laborator Electronica",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul D",
            "camera": "D105",
        },
        {
            "nume": "Sala Seminar E101",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul E",
            "camera": "E101",
        },
        {
            "nume": "Sala Seminar E204",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul E",
            "camera": "E204",
        },
        {
            "nume": "Biblioteca Universitatii",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul F",
            "camera": "Sala lectura",
        },
        {
            "nume": "Sala Conferinte",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul G",
            "camera": "G001",
        },
        {
            "nume": "Sala Sport",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Complex sportiv",
            "camera": "Sala principala",
        },
        {
            "nume": "Teren Fotbal",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Complex sportiv",
            "camera": "Exterior",
        },
        {
            "nume": "Sala Festivitati",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul A",
            "camera": "Sala festivitati",
        },
        {
            "nume": "Laborator Robotica",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul D",
            "camera": "D210",
        },
        {
            "nume": "Laborator Inteligenta Artificiala",
            "adresa": "Strada Universitatii nr. 13, Suceava",
            "cladire": "Corpul C",
            "camera": "C305",
        },
    ]


def default_eveniment_data():
    organizatie = OrganizatorRepository()
    locatie = LocatieRepository()
    categorie = CategorieRepository()
    stare = StareRepository()

    tip_participare = TipParticipareRepository()

    organizatie_id = organizatie.get_instance_by_name("FIRESC")

    locatie_id = locatie.get_instance_by_name("Laborator Calculatoare 1")

    categorie_id = categorie.get_instance_by_name("Tehnologie si IT")

    tip_participare_id = tip_participare.get_instance_by_name("Fizic")

    stare_id = stare.get_instance_by_name("Acceptat")

    return [
        {
            "nume": "Workshop Introducere in Inteligenta Artificiala",
            "descriere": "Eveniment organizat de asociatia FIRESC destinat studentilor interesati de domeniul inteligentei artificiale. In cadrul workshop-ului, participantii vor invata concepte de baza despre machine learning si vor implementa modele simple folosind Python.",
            "link": "https://www.facebook.com/firesc",
            "organizator": organizatie_id,
            "locatie": locatie_id,
            "categorie": categorie_id,
            "tip_participare": tip_participare_id,
            "start_data": timezone.make_aware(datetime(2026, 4, 15, 10, 0, 0)),
            "end_data": timezone.make_aware(datetime(2026, 4, 15, 14, 0, 0)),
            "capacitate": 25,
            "stare": stare_id,
        },
    ]


def default_sponsor_data():
    stare = StareRepository()

    stare_id = stare.get_instance_by_name("Activ")

    return [
        {
            "nume": "ASSIST Software",
            "descriere": "Companie IT de top din Suceava, specializata in dezvoltare software si solutii tehnologice inovatoare. Colaboreaza activ cu mediul academic si sustine evenimente dedicate studentilor.",
            "link": "https://assist-software.net",
            "stare": stare_id,
        },
        {
            "nume": "EGGER Romania",
            "descriere": "Companie internationala din industria prelucrarii lemnului, cu o prezenta puternica in Romania. Sustine initiative educationale si proiecte dedicate studentilor din domenii tehnice.",
            "link": "https://www.egger.com",
            "stare": stare_id,
        },
        {
            "nume": "Continental Automotive Romania",
            "descriere": "Companie multinationala specializata in tehnologii auto si sisteme inteligente de transport. Implicata in programe educationale si parteneriate cu universitati tehnice.",
            "link": "https://www.continental.com",
            "stare": stare_id,
        },
        {
            "nume": "Siemens Romania",
            "descriere": "Companie globala in domeniul ingineriei si tehnologiei, implicata in proiecte de digitalizare si automatizare. Sustine dezvoltarea profesionala a studentilor prin colaborari academice.",
            "link": "https://www.siemens.com/ro",
            "stare": stare_id,
        },
        {
            "nume": "Amazon Development Center Iasi",
            "descriere": "Centru de dezvoltare software al Amazon in Romania, implicat in proiecte globale si initiative educationale pentru studenti din domeniul IT.",
            "link": "https://www.amazon.jobs",
            "stare": stare_id,
        },
        {
            "nume": "Bitdefender",
            "descriere": "Companie romaneasca de top in domeniul securitatii cibernetice, recunoscuta international. Sustine educatia si dezvoltarea tinerilor in domeniul IT.",
            "link": "https://www.bitdefender.com",
            "stare": stare_id,
        },
        {
            "nume": "Endava Romania",
            "descriere": "Companie de servicii IT si consultanta, implicata in dezvoltarea de solutii software si in programe de mentorat si training pentru studenti.",
            "link": "https://www.endava.com",
            "stare": stare_id,
        },
    ]


def default_sponsor_eveniment_data():
    sponsor = SponsorRepository()
    eveniment = EvenimentRepository()

    sponsor_id = sponsor.get_instance_by_name("ASSIST Software")
    sponsor1_id = sponsor.get_instance_by_name("EGGER Romania")
    sponsor2_id = sponsor.get_instance_by_name("Continental Automotive Romania")
    sponsor3_id = sponsor.get_instance_by_name("Siemens Romania")
    sponsor4_id = sponsor.get_instance_by_name("Amazon Development Center Iasi")
    sponsor5_id = sponsor.get_instance_by_name("Bitdefender")
    sponsor6_id = sponsor.get_instance_by_name("Endava Romania")

    eveniment_id = eveniment.get_instance_by_name(
        "Workshop Introducere in Inteligenta Artificiala"
    )

    return [
        {
            "sponsor": sponsor_id,
            "eveniment": eveniment_id,
        },
        {
            "sponsor": sponsor1_id,
            "eveniment": eveniment_id,
        },
        {
            "sponsor": sponsor2_id,
            "eveniment": eveniment_id,
        },
        {
            "sponsor": sponsor3_id,
            "eveniment": eveniment_id,
        },
        {
            "sponsor": sponsor4_id,
            "eveniment": eveniment_id,
        },
        {
            "sponsor": sponsor5_id,
            "eveniment": eveniment_id,
        },
        {
            "sponsor": sponsor6_id,
            "eveniment": eveniment_id,
        },
    ]


def default_inregistrare_data():
    user = UserRepository()
    eveniment = EvenimentRepository()
    stare = StareRepository()

    user_id = user.get_instance_by_username("student")

    eveniment_id = eveniment.get_instance_by_name(
        "Workshop Introducere in Inteligenta Artificiala"
    )

    stare_id = stare.get_instance_by_name("Acceptat")

    return [
        {
            "user": user_id,
            "eveniment": eveniment_id,
            "stare": stare_id,
        },
    ]
