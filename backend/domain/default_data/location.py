def default_location_data():
    """
    Returnează lista locațiilor default
    utilizate pentru popularea inițială a bazei de date.

    Locațiile includ:
    - săli de curs,
    - amfiteatre,
    - laboratoare,
    - săli sportive,
    - locații online,
    - spații administrative.
    """

    return [
        # =====================================================
        # CORP A
        # =====================================================
        {
            "name": "Aula Magna",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul A",
            "room": "Aula",
        },
        {
            "name": "Amfiteatru Corp A",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul A",
            "room": "Amfiteatru",
        },
        {
            "name": "Sala curs Corp A",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul A",
            "room": "Sala curs",
        },
        {
            "name": "Sala seminar Corp A",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul A",
            "room": "Sala seminar",
        },
        # =====================================================
        # CORP B
        # =====================================================
        {
            "name": "Amfiteatru FIM 1",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul B",
            "room": "FIM 1",
        },
        {
            "name": "Amfiteatru FIM 2",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul B",
            "room": "FIM 2",
        },
        {
            "name": "Sala Consiliu B214",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul B",
            "room": "B214",
        },
        {
            "name": "Sala curs Corp B",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul B",
            "room": "Sala curs",
        },
        # =====================================================
        # CORP C2
        # =====================================================
        {
            "name": "Sala curs Corp C2",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul C2",
            "room": "Sala curs",
        },
        # =====================================================
        # CORP D
        # =====================================================
        {
            "name": "Laborator Calculatoare",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul D",
            "room": "Laborator 15 calculatoare",
        },
        {
            "name": "Amfiteatru FIESC",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul D",
            "room": "Amfiteatru FIESC",
        },
        {
            "name": "Sala D. Leonida",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul D",
            "room": "D. Leonida",
        },
        {
            "name": "Sala Consiliu Corp D",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul D",
            "room": "Sala consiliu",
        },
        {
            "name": "Sala seminar Corp D",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul D",
            "room": "Sala seminar",
        },
        # =====================================================
        # CORP E
        # =====================================================
        {
            "name": ("Secretariat Facultatea de Medicina " "si Stiinte Biologice"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul E",
            "room": "E011",
        },
        {
            "name": "Compartiment Acte de Studii",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul E",
            "room": "E138",
        },
        # =====================================================
        # CORP F
        # =====================================================
        {
            "name": "Auditorium Joseph Schmidt",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul F",
            "room": "Auditorium",
        },
        {
            "name": "Sala de sedinte Corp F",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul F",
            "room": "Sala de sedinte",
        },
        # =====================================================
        # CORP G
        # =====================================================
        {
            "name": ("Laborator de Compatibilitate " "Electromagnetica"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul G",
            "room": ("Laborator Compatibilitate " "Electromagnetica"),
        },
        # =====================================================
        # CORP J
        # =====================================================
        {
            "name": "Sala curs Corp J",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul J",
            "room": "Sala curs",
        },
        # =====================================================
        # COMPLEX NATATIE
        # =====================================================
        {
            "name": ("Complex de Natatie si Kinetoterapie " "- Sala K201"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": ("Complex Natatie si Kinetoterapie"),
            "room": "K201",
        },
        {
            "name": ("Complex de Natatie si Kinetoterapie " "- Sala K202"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": ("Complex Natatie si Kinetoterapie"),
            "room": "K202",
        },
        {
            "name": ("Complex de Natatie si Kinetoterapie " "- Sala K203"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": ("Complex Natatie si Kinetoterapie"),
            "room": "K203",
        },
        {
            "name": ("Complex de Natatie si Kinetoterapie " "- Sala K210"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": ("Complex Natatie si Kinetoterapie"),
            "room": "K210",
        },
        {
            "name": ("Complex de Natatie si Kinetoterapie " "- Bazin"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": ("Complex Natatie si Kinetoterapie"),
            "room": "Bazin",
        },
        {
            "name": ("Complex de Natatie si Kinetoterapie " "- Sala de forta"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": ("Complex Natatie si Kinetoterapie"),
            "room": "Sala de forta",
        },
        # =====================================================
        # COMPLEX SPORTIV
        # =====================================================
        {
            "name": "Sala de Sport",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Complex sportiv",
            "room": "Sala de sport",
        },
        {
            "name": "Teren de sport - Balon",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Complex sportiv",
            "room": "Teren de sport cu balon",
        },
        {
            "name": "Teren de sport neacoperit",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Complex sportiv",
            "room": "Teren de sport",
        },
        {
            "name": "Pista sportiva",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Complex sportiv",
            "room": "Pista",
        },
        # =====================================================
        # PLANETARIU
        # =====================================================
        {
            "name": ("Planetariu si Observator Astronomic"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": ("Planetariu si Observator Astronomic"),
            "room": "Sala principala",
        },
        # =====================================================
        # BIBLIOTECA
        # =====================================================
        {
            "name": ("Biblioteca USV - Sala de lectura 1"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Biblioteca USV",
            "room": "Sala de lectura 1",
        },
        {
            "name": ("Biblioteca USV - Sala de lectura 2"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Biblioteca USV",
            "room": "Sala de lectura 2",
        },
        {
            "name": ("Biblioteca USV - Sala multimedia"),
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Biblioteca USV",
            "room": "Sala multimedia",
        },
        # =====================================================
        # VATRA DORNEI
        # =====================================================
        {
            "name": ("CTIEC Vatra Dornei - Sala de sedinte"),
            "address": "Vatra Dornei",
            "building": ("Obiectiv CTIEC Vatra Dornei"),
            "room": "Sala de sedinte",
        },
        {
            "name": ("CTIEC Vatra Dornei - Sala fitness"),
            "address": "Vatra Dornei",
            "building": ("Obiectiv CTIEC Vatra Dornei"),
            "room": "Sala fitness",
        },
        # =====================================================
        # CAMPUS 2
        # =====================================================
        {
            "name": "Campus 2 Moara",
            "address": ("Comuna Moara, Judetul Suceava"),
            "building": "Campus 2",
            "room": "Sala evenimente",
        },
        # =====================================================
        # ONLINE
        # =====================================================
        {
            "name": "Online - Google Meet",
            "address": "Online",
            "building": "Online",
            "room": "Google Meet",
        },
        {
            "name": "Online - Microsoft Teams",
            "address": "Online",
            "building": "Online",
            "room": "Microsoft Teams",
        },
        {
            "name": "Online - Zoom",
            "address": "Online",
            "building": "Online",
            "room": "Zoom",
        },
        # =====================================================
        # LABORATOARE
        # =====================================================
        {
            "name": "Laborator Calculatoare 1",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul C",
            "room": "C201",
        },
        {
            "name": "Laborator Inteligenta Artificiala",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Corpul C",
            "room": "C305",
        },
        # =====================================================
        # SPORT
        # =====================================================
        {
            "name": "Sala Sport",
            "address": ("Strada Universitatii nr. 13, " "720229 Suceava"),
            "building": "Complex sportiv",
            "room": "Sala principala",
        },
    ]
