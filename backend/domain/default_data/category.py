def default_category_data():
    """
    Returnează lista de categorii default
    folosite pentru popularea inițială a bazei de date.

    Fiecare categorie conține:
    - name
    - description
    """

    return [
        # =====================================================
        # SPORT
        # =====================================================
        {
            "name": "Sport si activitati fizice",
            "description": (
                "Sports competitions, tournaments, " "fitness and physical activities."
            ),
        },
        # =====================================================
        # EDUCATIE
        # =====================================================
        {
            "name": "Educatie si formare",
            "description": (
                "Courses, trainings, seminars " "and educational activities."
            ),
        },
        # =====================================================
        # TEHNOLOGIE
        # =====================================================
        {
            "name": "Tehnologie si IT",
            "description": (
                "Technology events, programming workshops, "
                "hackathons and IT presentations."
            ),
        },
        # =====================================================
        # CULTURA
        # =====================================================
        {
            "name": "Cultura si arta",
            "description": (
                "Cultural events, exhibitions, theatre, "
                "music and artistic activities."
            ),
        },
        # =====================================================
        # CARIERA
        # =====================================================
        {
            "name": "Cariera si dezvoltare profesionala",
            "description": (
                "Career fairs, networking events, "
                "internships and company presentations."
            ),
        },
        # =====================================================
        # VOLUNTARIAT
        # =====================================================
        {
            "name": "Voluntariat si comunitate",
            "description": (
                "Volunteering, charity and " "community involvement activities."
            ),
        },
        # =====================================================
        # SOCIAL
        # =====================================================
        {
            "name": "Social si divertisment",
            "description": (
                "Social gatherings, parties, games " "and entertainment activities."
            ),
        },
        # =====================================================
        # CONFERINTA
        # =====================================================
        {
            "name": "Conferinta academica",
            "description": (
                "Scientific conferences, symposiums " "and academic presentations."
            ),
        },
        # =====================================================
        # WORKSHOP
        # =====================================================
        {
            "name": "Workshop practic",
            "description": (
                "Hands-on practical workshops " "and applied learning sessions."
            ),
        },
        # =====================================================
        # HACKATHON
        # =====================================================
        {
            "name": "Hackathon",
            "description": (
                "Collaborative programming and " "innovation competitions."
            ),
        },
        # =====================================================
        # COMPETITII
        # =====================================================
        {
            "name": "Competitie studenteasca",
            "description": (
                "Student contests, olympiads " "and academic competitions."
            ),
        },
        # =====================================================
        # CERCETARE
        # =====================================================
        {
            "name": "Cercetare si inovatie",
            "description": (
                "Research projects, innovation showcases " "and scientific discussions."
            ),
        },
        # =====================================================
        # ANTREPRENORIAT
        # =====================================================
        {
            "name": "Antreprenoriat si business",
            "description": (
                "Startup, entrepreneurship " "and business-oriented events."
            ),
        },
        # =====================================================
        # LEADERSHIP
        # =====================================================
        {
            "name": "Leadership si dezvoltare personala",
            "description": (
                "Leadership, communication and " "self-development activities."
            ),
        },
        # =====================================================
        # SANATATE
        # =====================================================
        {
            "name": "Sanatate si wellbeing",
            "description": ("Health awareness, wellbeing " "and mental health events."),
        },
        # =====================================================
        # MEDICINA
        # =====================================================
        {
            "name": "Medicina si stiinte biologice",
            "description": (
                "Medical, healthcare and biological sciences " "related activities."
            ),
        },
        # =====================================================
        # INGINERIE
        # =====================================================
        {
            "name": "Inginerie si robotica",
            "description": ("Engineering, robotics and automation " "related events."),
        },
        # =====================================================
        # ELECTRONICA
        # =====================================================
        {
            "name": "Electronica si automatizari",
            "description": (
                "Electronics, embedded systems " "and automation activities."
            ),
        },
        # =====================================================
        # AI
        # =====================================================
        {
            "name": "Inteligenta artificiala si machine learning",
            "description": (
                "Artificial intelligence, deep learning " "and data science events."
            ),
        },
        # =====================================================
        # CYBERSECURITY
        # =====================================================
        {
            "name": "Cybersecurity",
            "description": (
                "Cybersecurity, ethical hacking " "and information security activities."
            ),
        },
        # =====================================================
        # GAME DEV
        # =====================================================
        {
            "name": "Game development",
            "description": (
                "Game development, game design " "and interactive technologies."
            ),
        },
        # =====================================================
        # DESIGN
        # =====================================================
        {
            "name": "Design si multimedia",
            "description": (
                "Graphic design, UI/UX, video " "and multimedia activities."
            ),
        },
        # =====================================================
        # MARKETING
        # =====================================================
        {
            "name": "Marketing si comunicare",
            "description": (
                "Marketing, branding, social media " "and communication events."
            ),
        },
        # =====================================================
        # EDUCATIE FINANCIARA
        # =====================================================
        {
            "name": "Educatie financiara",
            "description": (
                "Financial education, investments " "and economic awareness activities."
            ),
        },
        # =====================================================
        # DREPT
        # =====================================================
        {
            "name": "Drept si administratie publica",
            "description": (
                "Law, public administration and " "civic education events."
            ),
        },
        # =====================================================
        # PSIHOLOGIE
        # =====================================================
        {
            "name": "Psihologie si dezvoltare umana",
            "description": (
                "Psychology, counselling and " "human development activities."
            ),
        },
        # =====================================================
        # ECOLOGIE
        # =====================================================
        {
            "name": "Ecologie si sustenabilitate",
            "description": (
                "Environmental protection, sustainability " "and green initiatives."
            ),
        },
        # =====================================================
        # SILVICULTURA
        # =====================================================
        {
            "name": "Silvicultura si mediu",
            "description": (
                "Forestry, biodiversity and " "environmental management events."
            ),
        },
        # =====================================================
        # ISTORIE
        # =====================================================
        {
            "name": "Istorie si stiinte sociale",
            "description": (
                "History, sociology, geopolitics " "and social sciences discussions."
            ),
        },
        # =====================================================
        # LITERATURA
        # =====================================================
        {
            "name": "Literatura si limbi straine",
            "description": (
                "Literature, linguistics and " "foreign language activities."
            ),
        },
        # =====================================================
        # FESTIVAL
        # =====================================================
        {
            "name": "Festival si evenimente speciale",
            "description": (
                "Festivals, anniversary celebrations " "and major university events."
            ),
        },
        # =====================================================
        # INTERNATIONAL
        # =====================================================
        {
            "name": "Eveniment international",
            "description": (
                "International collaborations, Erasmus " "and multicultural events."
            ),
        },
        # =====================================================
        # COMPANII
        # =====================================================
        {
            "name": "Prezentare companie",
            "description": (
                "Company presentations, recruitment sessions " "and employer branding."
            ),
        },
        # =====================================================
        # TARG EDUCATIONAL
        # =====================================================
        {
            "name": "Targ educational",
            "description": (
                "Educational fairs, student recruitment "
                "and academic promotion activities."
            ),
        },
        # =====================================================
        # NETWORKING
        # =====================================================
        {
            "name": "Sesiune de networking",
            "description": (
                "Networking and professional relationship " "building events."
            ),
        },
        # =====================================================
        # WEBINAR
        # =====================================================
        {
            "name": "Webinar",
            "description": ("Online educational or professional " "virtual sessions."),
        },
        # =====================================================
        # PODCAST
        # =====================================================
        {
            "name": "Podcast si media",
            "description": (
                "Media production, podcasting " "and journalism related activities."
            ),
        },
        # =====================================================
        # FOTO / FILM
        # =====================================================
        {
            "name": "Fotografie si film",
            "description": (
                "Photography, cinematography " "and video production events."
            ),
        },
        # =====================================================
        # MUZICA
        # =====================================================
        {
            "name": "Muzica si spectacol",
            "description": ("Concerts, music festivals " "and live performances."),
        },
        # =====================================================
        # GAMING
        # =====================================================
        {
            "name": "Gaming si esports",
            "description": (
                "Gaming tournaments, esports " "and gaming community activities."
            ),
        },
        # =====================================================
        # DEZBATERI
        # =====================================================
        {
            "name": "Dezbateri si discurs public",
            "description": (
                "Debates, public speaking " "and argumentation activities."
            ),
        },
        # =====================================================
        # RELATII INTERNATIONALE
        # =====================================================
        {
            "name": "Relatii internationale",
            "description": (
                "International relations, diplomacy " "and European studies events."
            ),
        },
        # =====================================================
        # RELIGIE
        # =====================================================
        {
            "name": "Religie si spiritualitate",
            "description": (
                "Religious, spiritual and ethical " "discussions or activities."
            ),
        },
        # =====================================================
        # ORIENTARE CARIERA
        # =====================================================
        {
            "name": "Orientare in cariera",
            "description": (
                "Career guidance, CV workshops " "and interview preparation."
            ),
        },
        # =====================================================
        # PRACTICA
        # =====================================================
        {
            "name": "Practica si internship",
            "description": (
                "Internship programs, practical training " "and industry collaboration."
            ),
        },
        # =====================================================
        # DIGITAL
        # =====================================================
        {
            "name": "Inovare digitala",
            "description": ("Digital transformation and " "innovation related events."),
        },
        # =====================================================
        # OPEN DAY
        # =====================================================
        {
            "name": "Open day",
            "description": ("University open days and " "faculty presentation events."),
        },
        # =====================================================
        # ADMITERE
        # =====================================================
        {
            "name": "Admitere si informare",
            "description": (
                "Admission guidance and informational " "events for future students."
            ),
        },
        # =====================================================
        # ELEVI
        # =====================================================
        {
            "name": "Activitati pentru elevi",
            "description": (
                "Educational and interactive activities "
                "dedicated to high school students."
            ),
        },
        # =====================================================
        # SPORTIV
        # =====================================================
        {
            "name": "Competitie sportiva",
            "description": (
                "Organized sports championships " "and athletic competitions."
            ),
        },
        # =====================================================
        # TEAM BUILDING
        # =====================================================
        {
            "name": "Team building",
            "description": ("Team cohesion and collaboration activities."),
        },
    ]
