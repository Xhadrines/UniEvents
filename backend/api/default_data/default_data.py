from datetime import datetime, timedelta
from django.utils import timezone

from ..repository import (
    UserRepository,
    FacultyRepository,
    SpecializationRepository,
    RoleRepository,
    StatusRepository,
    UserProfileRepository,
    OrganizerTypeRepository,
    OrganizerRepository,
    CategoryRepository,
    ParticipationTypeRepository,
    LocationRepository,
    EventRepository,
    SponsorRepository,
    EventSponsorRepository,
    RegistrationRepository,
    FeedbackRepository,
    MaterialTypeRepository,
    EventMaterialRepository,
    FavoriteEventRepository,
    NotificationTypeRepository,
    NotificationRepository,
    ReportRepository,
)


def aware(year, month, day, hour, minute=0):
    # Creeaza o data timezone-aware
    return timezone.make_aware(datetime(year, month, day, hour, minute, 0))


def default_user_data():
    return [
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
    ]


def default_role_data():
    return [
        {
            "name": "Administrator",
            "description": "Role with full permissions for users, events, reports and validations.",
        },
        {
            "name": "Student",
            "description": "Role for students who can view events, register and add feedback.",
        },
        {
            "name": "Profesor",
            "description": "Role for teachers who can organize university events.",
        },
        {
            "name": "Partener",
            "description": "Role for external partners involved in events and sponsorships.",
        },
        {
            "name": "Organizatie",
            "description": "Role for student associations, clubs and organizations.",
        },
        {
            "name": "Altele",
            "description": "Generic role for users that do not match the standard categories.",
        },
    ]


def default_status_data():
    return [
        {
            "name": "Activ",
            "description": "Entity is active and can be used.",
        },
        {
            "name": "Inactiv",
            "description": "Entity is inactive but can be reactivated.",
        },
        {
            "name": "Sters",
            "description": "Entity is marked as deleted.",
        },
        {
            "name": "In asteptare",
            "description": "Entity is waiting for validation or approval.",
        },
        {
            "name": "Anulat",
            "description": "Entity was cancelled.",
        },
        {
            "name": "Respins",
            "description": "Entity was rejected.",
        },
        {
            "name": "Acceptat",
            "description": "Entity was accepted or approved.",
        },
        {
            "name": "Lista de asteptare",
            "description": "Registration is placed on the waiting list.",
        },
        {
            "name": "Finalizat",
            "description": "Event or process is finished.",
        },
    ]


def default_faculty_data():
    return [
        {"name": "Facultatea de Drept si Stiinte Administrative"},
        {"name": "Facultatea de Economie, Administratie si Afaceri"},
        {"name": "Facultatea de Educatie Fizica si Sport"},
        {"name": "Facultatea de Inginerie Alimentara"},
        {"name": "Facultatea de Inginerie Electrica si Stiinta Calculatoarelor"},
        {"name": "Facultatea de Inginerie Mecanica, Autovehicule si Robotica"},
        {"name": "Facultatea de Istorie, Geografie si Stiinte Sociale"},
        {"name": "Facultatea de Litere si Stiinte ale Comunicarii"},
        {"name": "Facultatea de Medicina si Stiinte Biologice"},
        {"name": "Facultatea de Psihologie si Stiinte ale Educatiei"},
        {"name": "Facultatea de Silvicultura"},
    ]


def default_specialization_data():
    faculty_repository = FacultyRepository()

    faculty = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Electrica si Stiinta Calculatoarelor"
    )

    return [
        {"name": "Calculatoare", "faculty": faculty},
        {"name": "Electronica aplicata", "faculty": faculty},
        {"name": "Retele si software de telecomunicatii", "faculty": faculty},
        {"name": "Sisteme electrice", "faculty": faculty},
        {"name": "Energetica si tehnologii informatice", "faculty": faculty},
        {"name": "Managementul energiei", "faculty": faculty},
        {"name": "Automatica si informatica aplicata", "faculty": faculty},
        {
            "name": "Echipamente si sisteme de comanda si control pentru autovehicule",
            "faculty": faculty,
        },
        {"name": "Echipamente si sisteme medicale", "faculty": faculty},
    ]


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


def default_organizer_type_data():
    return [
        {
            "name": "Asociatie de studenti",
            "description": "Student association that organizes events for students.",
        },
        {
            "name": "Profesor",
            "description": "Teacher or academic staff organizer.",
        },
        {
            "name": "Club universitar",
            "description": "University club that organizes academic or social activities.",
        },
        {
            "name": "Partener extern",
            "description": "External company or institution involved in university events.",
        },
    ]


def default_organizer_data():
    user_repository = UserRepository()
    status_repository = StatusRepository()
    organizer_type_repository = OrganizerTypeRepository()
    faculty_repository = FacultyRepository()

    active_status = status_repository.get_instance_by_name("Activ")
    faculty = faculty_repository.get_instance_by_name(
        "Facultatea de Inginerie Electrica si Stiinta Calculatoarelor"
    )

    return [
        {
            "name": "FIRESC",
            "description": "Student association from FIESC focused on events, workshops and student activities.",
            "link": "https://www.facebook.com/firesc",
            "organizer_type": organizer_type_repository.get_instance_by_name(
                "Asociatie de studenti"
            ),
            "user": user_repository.get_instance_by_username("organization"),
            "status": active_status,
            "faculty": faculty,
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
            "faculty": faculty,
        },
    ]


def default_category_data():
    return [
        {
            "name": "Sport si activitati fizice",
            "description": "Sports, competitions and physical activities.",
        },
        {
            "name": "Educatie si formare",
            "description": "Courses, trainings, seminars and learning activities.",
        },
        {
            "name": "Tehnologie si IT",
            "description": "Technology events, workshops, hackathons and IT presentations.",
        },
        {
            "name": "Cultura si arta",
            "description": "Cultural events, exhibitions, shows and artistic activities.",
        },
        {
            "name": "Cariera si dezvoltare profesionala",
            "description": "Career fairs, networking sessions and company presentations.",
        },
        {
            "name": "Voluntariat si comunitate",
            "description": "Volunteering and community involvement events.",
        },
        {
            "name": "Social si divertisment",
            "description": "Social, recreational and entertainment events.",
        },
    ]


def default_participation_type_data():
    return [
        {
            "name": "Fizic",
            "description": "Participants attend the event at the physical location.",
        },
        {
            "name": "Online",
            "description": "Participants attend the event through an online platform.",
        },
        {
            "name": "Hibrid",
            "description": "Participants can attend either physically or online.",
        },
    ]


def default_location_data():
    return [
        {
            "name": "Aula Magna",
            "address": "Strada Universitatii nr. 13, Suceava",
            "building": "Corpul A",
            "room": "Aula Magna",
        },
        {
            "name": "Laborator Calculatoare 1",
            "address": "Strada Universitatii nr. 13, Suceava",
            "building": "Corpul C",
            "room": "C201",
        },
        {
            "name": "Laborator Inteligenta Artificiala",
            "address": "Strada Universitatii nr. 13, Suceava",
            "building": "Corpul C",
            "room": "C305",
        },
        {
            "name": "Sala Sport",
            "address": "Strada Universitatii nr. 13, Suceava",
            "building": "Complex sportiv",
            "room": "Sala principala",
        },
        {
            "name": "Online - Google Meet",
            "address": "Online",
            "building": "Online",
            "room": "Google Meet",
        },
    ]


def default_event_data():
    user_repository = UserRepository()
    organizer_repository = OrganizerRepository()
    location_repository = LocationRepository()
    category_repository = CategoryRepository()
    participation_type_repository = ParticipationTypeRepository()
    status_repository = StatusRepository()

    accepted_status = status_repository.get_instance_by_name("Acceptat")
    pending_status = status_repository.get_instance_by_name("In asteptare")
    finished_status = status_repository.get_instance_by_name("Finalizat")
    admin_user = user_repository.get_instance_by_username("administrator")

    return [
        {
            "name": "Workshop Introducere in Inteligenta Artificiala",
            "description": "Workshop practic pentru studenti interesati de AI, machine learning si Python.",
            "registration_link": "https://example.com/register/ai-workshop",
            "online_link": None,
            "organizer": organizer_repository.get_instance_by_name("FIRESC"),
            "location": location_repository.get_instance_by_name(
                "Laborator Inteligenta Artificiala"
            ),
            "category": category_repository.get_instance_by_name("Tehnologie si IT"),
            "participation_type": participation_type_repository.get_instance_by_name(
                "Fizic"
            ),
            "status": finished_status,
            "start_date": aware(2026, 4, 15, 10),
            "end_date": aware(2026, 4, 15, 14),
            "capacity": 25,
            "registration_deadline": aware(2026, 4, 14, 23, 59),
            "is_free_entry": True,
            "requires_registration": True,
            "requires_ticket": True,
            "qr_code": "events/qr_codes/ai_workshop.png",
            "max_files": 5,
            "max_file_size_mb": 20,
            "validated_by": admin_user,
            "validated_at": aware(2026, 4, 1, 12),
        },
        {
            "name": "Targ de Cariere USV 2026",
            "description": "Eveniment dedicat studentilor care doresc stagii, joburi si discutii cu angajatori.",
            "registration_link": "https://example.com/register/career-fair",
            "online_link": None,
            "organizer": organizer_repository.get_instance_by_name(
                "USV Computer Science Department"
            ),
            "location": location_repository.get_instance_by_name("Aula Magna"),
            "category": category_repository.get_instance_by_name(
                "Cariera si dezvoltare profesionala"
            ),
            "participation_type": participation_type_repository.get_instance_by_name(
                "Fizic"
            ),
            "status": accepted_status,
            "start_date": aware(2026, 6, 10, 9),
            "end_date": aware(2026, 6, 10, 16),
            "capacity": 300,
            "registration_deadline": aware(2026, 6, 9, 23, 59),
            "is_free_entry": True,
            "requires_registration": False,
            "requires_ticket": False,
            "qr_code": "events/qr_codes/career_fair.png",
            "max_files": 10,
            "max_file_size_mb": 50,
            "validated_by": admin_user,
            "validated_at": aware(2026, 5, 1, 10),
        },
        {
            "name": "Seminar Online Cybersecurity",
            "description": "Seminar online despre bune practici de securitate cibernetica.",
            "registration_link": "https://example.com/register/cybersecurity",
            "online_link": "https://meet.google.com/demo-cybersecurity",
            "organizer": organizer_repository.get_instance_by_name("FIRESC"),
            "location": location_repository.get_instance_by_name(
                "Online - Google Meet"
            ),
            "category": category_repository.get_instance_by_name("Tehnologie si IT"),
            "participation_type": participation_type_repository.get_instance_by_name(
                "Online"
            ),
            "status": pending_status,
            "start_date": aware(2026, 7, 5, 18),
            "end_date": aware(2026, 7, 5, 20),
            "capacity": 100,
            "registration_deadline": aware(2026, 7, 4, 23, 59),
            "is_free_entry": True,
            "requires_registration": True,
            "requires_ticket": False,
            "max_files": 3,
            "max_file_size_mb": 10,
        },
    ]


def default_sponsor_data():
    status_repository = StatusRepository()
    active_status = status_repository.get_instance_by_name("Activ")

    return [
        {
            "name": "ASSIST Software",
            "description": "Software company from Suceava involved in educational events.",
            "link": "https://assist-software.net",
            "logo": "sponsors/logos/assist.png",
            "status": active_status,
        },
        {
            "name": "EGGER Romania",
            "description": "International wood processing company supporting student initiatives.",
            "link": "https://www.egger.com",
            "logo": "sponsors/logos/egger.png",
            "status": active_status,
        },
        {
            "name": "Bitdefender",
            "description": "Romanian cybersecurity company supporting IT education.",
            "link": "https://www.bitdefender.com",
            "logo": "sponsors/logos/bitdefender.png",
            "status": active_status,
        },
    ]


def default_event_sponsor_data():
    sponsor_repository = SponsorRepository()
    event_repository = EventRepository()

    ai_event = event_repository.get_instance_by_name(
        "Workshop Introducere in Inteligenta Artificiala"
    )
    career_event = event_repository.get_instance_by_name("Targ de Cariere USV 2026")

    return [
        {
            "sponsor": sponsor_repository.get_instance_by_name("ASSIST Software"),
            "event": ai_event,
        },
        {
            "sponsor": sponsor_repository.get_instance_by_name("Bitdefender"),
            "event": ai_event,
        },
        {
            "sponsor": sponsor_repository.get_instance_by_name("EGGER Romania"),
            "event": career_event,
        },
    ]


def default_registration_data():
    user_repository = UserRepository()
    event_repository = EventRepository()
    status_repository = StatusRepository()

    accepted_status = status_repository.get_instance_by_name("Acceptat")
    waiting_status = status_repository.get_instance_by_name("Lista de asteptare")

    return [
        {
            "user": user_repository.get_instance_by_username("student"),
            "event": event_repository.get_instance_by_name(
                "Workshop Introducere in Inteligenta Artificiala"
            ),
            "status": accepted_status,
            "confirmation_email_sent": True,
            "ticket_qr_code": "tickets/qr_codes/student_ai_workshop.png",
            "checked_in": True,
            "checked_in_at": aware(2026, 4, 15, 9, 55),
        },
        {
            "user": user_repository.get_instance_by_username("guest"),
            "event": event_repository.get_instance_by_name("Targ de Cariere USV 2026"),
            "status": waiting_status,
            "confirmation_email_sent": False,
            "checked_in": False,
        },
    ]


def default_feedback_data():
    user_repository = UserRepository()
    event_repository = EventRepository()

    return [
        {
            "user": user_repository.get_instance_by_username("student"),
            "event": event_repository.get_instance_by_name(
                "Workshop Introducere in Inteligenta Artificiala"
            ),
            "rating": 5,
            "comment": "Workshop foarte util, cu exemple clare si aplicatii practice.",
            "sentiment_score": 0.92,
            "sentiment_label": "positive",
        },
        {
            "user": user_repository.get_instance_by_username("guest"),
            "event": event_repository.get_instance_by_name(
                "Workshop Introducere in Inteligenta Artificiala"
            ),
            "rating": 4,
            "comment": "Eveniment bun, dar ar fi fost util mai mult timp pentru exercitii.",
            "sentiment_score": 0.65,
            "sentiment_label": "positive",
        },
    ]


def default_material_type_data():
    return [
        {
            "name": "PDF",
            "description": "PDF document.",
        },
        {
            "name": "Presentation",
            "description": "Slides or presentation file.",
        },
        {
            "name": "Image",
            "description": "Image file.",
        },
        {
            "name": "Archive",
            "description": "Compressed archive with resources.",
        },
    ]


def default_event_material_data():
    user_repository = UserRepository()
    event_repository = EventRepository()
    material_type_repository = MaterialTypeRepository()

    ai_event = event_repository.get_instance_by_name(
        "Workshop Introducere in Inteligenta Artificiala"
    )

    return [
        {
            "event": ai_event,
            "material_type": material_type_repository.get_instance_by_name("PDF"),
            "title": "AI Workshop Support Document",
            "file": "event_materials/ai_workshop_support.pdf",
            "is_public": True,
            "uploaded_by": user_repository.get_instance_by_username("professor"),
        },
        {
            "event": ai_event,
            "material_type": material_type_repository.get_instance_by_name(
                "Presentation"
            ),
            "title": "Introduction to Machine Learning Slides",
            "file": "event_materials/ml_intro_slides.pdf",
            "is_public": True,
            "uploaded_by": user_repository.get_instance_by_username("organization"),
        },
    ]


def default_favorite_event_data():
    user_repository = UserRepository()
    event_repository = EventRepository()

    return [
        {
            "user": user_repository.get_instance_by_username("student"),
            "event": event_repository.get_instance_by_name("Targ de Cariere USV 2026"),
        },
        {
            "user": user_repository.get_instance_by_username("guest"),
            "event": event_repository.get_instance_by_name(
                "Seminar Online Cybersecurity"
            ),
        },
    ]


def default_notification_type_data():
    return [
        {
            "name": "Reminder",
            "description": "Reminder before an event starts.",
        },
        {
            "name": "Registration Confirmation",
            "description": "Confirmation after event registration.",
        },
        {
            "name": "Event Update",
            "description": "Notification for event changes.",
        },
        {
            "name": "Event Cancelled",
            "description": "Notification for cancelled events.",
        },
    ]


def default_notification_data():
    user_repository = UserRepository()
    event_repository = EventRepository()
    notification_type_repository = NotificationTypeRepository()

    student = user_repository.get_instance_by_username("student")
    event = event_repository.get_instance_by_name("Targ de Cariere USV 2026")

    return [
        {
            "user": student,
            "event": event,
            "notification_type": notification_type_repository.get_instance_by_name(
                "Reminder"
            ),
            "title": "Event reminder",
            "message": "Targ de Cariere USV 2026 starts tomorrow.",
            "scheduled_at": aware(2026, 6, 9, 9),
            "sent_at": None,
            "is_read": False,
        },
        {
            "user": student,
            "event": event_repository.get_instance_by_name(
                "Workshop Introducere in Inteligenta Artificiala"
            ),
            "notification_type": notification_type_repository.get_instance_by_name(
                "Registration Confirmation"
            ),
            "title": "Registration confirmed",
            "message": "Your registration was confirmed.",
            "scheduled_at": None,
            "sent_at": timezone.now(),
            "is_read": True,
        },
    ]


def default_report_data():
    user_repository = UserRepository()

    return [
        {
            "generated_by": user_repository.get_instance_by_username("administrator"),
            "title": "Monthly Events Report",
            "description": "Report containing number of events, average participation and organizer activity.",
            "file": "reports/monthly_events_report.pdf",
        },
        {
            "generated_by": user_repository.get_instance_by_username("administrator"),
            "title": "Organizer Activity Report",
            "description": "Report for events organized by FIRESC.",
            "file": "reports/organizer_firesc_report.pdf",
        },
    ]


def default_email_token_data():
    user_repository = UserRepository()

    return [
        {
            "user": user_repository.get_instance_by_username("student"),
            "is_used": False,
        },
        {
            "user": user_repository.get_instance_by_username("guest"),
            "is_used": True,
        },
    ]
