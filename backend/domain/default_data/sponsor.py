from api.repository import StatusRepository


def default_sponsor_data():
    """
    Returnează lista sponsorilor default
    utilizați în aplicație.

    Sponsorii sunt utilizați pentru:
    - evenimente universitare,
    - workshop-uri,
    - conferințe,
    - activități educaționale și de recrutare.
    """

    # =====================================================
    # REPOSITORY
    # =====================================================

    status_repository = StatusRepository()

    # =====================================================
    # STATUS
    # =====================================================

    active_status = status_repository.get_instance_by_name("Activ")

    return [
        # =====================================================
        # ASSIST SOFTWARE
        # =====================================================
        {
            "name": "ASSIST Software",
            "description": (
                "Software company from Suceava involved "
                "in educational events, internships "
                "and workshops for students."
            ),
            "link": "https://assist-software.net",
            "logo": "sponsors/logos/assist.png",
            "status": active_status,
        },
        # =====================================================
        # EGGER
        # =====================================================
        {
            "name": "EGGER Romania",
            "description": (
                "International wood processing company "
                "supporting engineering and "
                "environmental initiatives."
            ),
            "link": "https://www.egger.com",
            "logo": "sponsors/logos/egger.png",
            "status": active_status,
        },
        # =====================================================
        # BITDEFENDER
        # =====================================================
        {
            "name": "Bitdefender",
            "description": (
                "Romanian cybersecurity company "
                "supporting IT education and "
                "security related events."
            ),
            "link": "https://www.bitdefender.com",
            "logo": ("sponsors/logos/bitdefender.png"),
            "status": active_status,
        },
        # =====================================================
        # MICROSOFT
        # =====================================================
        {
            "name": "Microsoft",
            "description": (
                "Technology company supporting "
                "software development and cloud "
                "computing education."
            ),
            "link": "https://www.microsoft.com",
            "logo": ("sponsors/logos/microsoft.png"),
            "status": active_status,
        },
        # =====================================================
        # AMAZON
        # =====================================================
        {
            "name": "Amazon",
            "description": (
                "Global technology company supporting "
                "educational and software engineering "
                "initiatives."
            ),
            "link": "https://www.amazon.com",
            "logo": "sponsors/logos/amazon.png",
            "status": active_status,
        },
        # =====================================================
        # IBM
        # =====================================================
        {
            "name": "IBM",
            "description": (
                "Technology and research company "
                "supporting innovation and "
                "artificial intelligence events."
            ),
            "link": "https://www.ibm.com",
            "logo": "sponsors/logos/ibm.png",
            "status": active_status,
        },
        # =====================================================
        # ORACLE
        # =====================================================
        {
            "name": "Oracle",
            "description": (
                "Enterprise software company involved "
                "in academic and database related "
                "initiatives."
            ),
            "link": "https://www.oracle.com",
            "logo": "sponsors/logos/oracle.png",
            "status": active_status,
        },
        # =====================================================
        # ENDAVA
        # =====================================================
        {
            "name": "Endava",
            "description": (
                "Software engineering company supporting "
                "student career development and IT events."
            ),
            "link": "https://www.endava.com",
            "logo": "sponsors/logos/endava.png",
            "status": active_status,
        },
        # =====================================================
        # BOSCH
        # =====================================================
        {
            "name": "Bosch Romania",
            "description": (
                "Technology and engineering company "
                "supporting innovation and "
                "technical education."
            ),
            "link": "https://www.bosch.ro",
            "logo": "sponsors/logos/bosch.png",
            "status": active_status,
        },
        # =====================================================
        # CONTINENTAL
        # =====================================================
        {
            "name": "Continental",
            "description": (
                "Engineering and automotive technology "
                "company involved in student recruitment "
                "and workshops."
            ),
            "link": ("https://www.continental.com"),
            "logo": ("sponsors/logos/continental.png"),
            "status": active_status,
        },
        # =====================================================
        # NTT DATA
        # =====================================================
        {
            "name": "NTT DATA Romania",
            "description": (
                "IT services company collaborating "
                "in educational and recruitment "
                "initiatives."
            ),
            "link": "https://ro.nttdata.com",
            "logo": ("sponsors/logos/ntt_data.png"),
            "status": active_status,
        },
        # =====================================================
        # ING HUBS
        # =====================================================
        {
            "name": "ING Hubs Romania",
            "description": (
                "Technology and financial services "
                "company supporting innovation "
                "and career events."
            ),
            "link": "https://inghubs.ro",
            "logo": ("sponsors/logos/ing_hubs.png"),
            "status": active_status,
        },
        # =====================================================
        # ORANGE
        # =====================================================
        {
            "name": "Orange Romania",
            "description": (
                "Telecommunications company supporting "
                "networking and communication "
                "technologies education."
            ),
            "link": "https://www.orange.ro",
            "logo": "sponsors/logos/orange.png",
            "status": active_status,
        },
        # =====================================================
        # VODAFONE
        # =====================================================
        {
            "name": "Vodafone Romania",
            "description": (
                "Telecommunications company involved "
                "in technology and connectivity initiatives."
            ),
            "link": "https://www.vodafone.ro",
            "logo": ("sponsors/logos/vodafone.png"),
            "status": active_status,
        },
        # =====================================================
        # BCR
        # =====================================================
        {
            "name": "BCR",
            "description": (
                "Banking institution supporting "
                "entrepreneurship and financial "
                "education events."
            ),
            "link": "https://www.bcr.ro",
            "logo": "sponsors/logos/bcr.png",
            "status": active_status,
        },
        # =====================================================
        # BRD
        # =====================================================
        {
            "name": "BRD",
            "description": (
                "Bank supporting student development " "and educational activities."
            ),
            "link": "https://www.brd.ro",
            "logo": "sponsors/logos/brd.png",
            "status": active_status,
        },
        # =====================================================
        # RAIFFEISEN
        # =====================================================
        {
            "name": "Raiffeisen Bank",
            "description": (
                "Financial institution supporting "
                "career and entrepreneurship events."
            ),
            "link": ("https://www.raiffeisen.ro"),
            "logo": ("sponsors/logos/raiffeisen.png"),
            "status": active_status,
        },
        # =====================================================
        # USV
        # =====================================================
        {
            "name": "USV",
            "description": (
                "Universitatea Stefan cel Mare "
                "din Suceava supporting academic "
                "and student events."
            ),
            "link": "https://www.usv.ro",
            "logo": "sponsors/logos/usv.png",
            "status": active_status,
        },
    ]
