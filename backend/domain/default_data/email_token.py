from api.repository import UserRepository


def default_email_token_data():
    """
    Returnează datele default pentru token-urile email.

    Aceste date sunt folosite pentru:
    - seed inițial,
    - testare,
    - dezvoltare locală.
    """

    # Inițializăm repository-ul utilizatorilor.
    user_repository = UserRepository()

    return [
        # =====================================================
        # TOKEN PENTRU STUDENT
        # =====================================================
        {
            # Asociem token-ul utilizatorului "student".
            "user": user_repository.get_instance_by_username("student"),
            # Token-ul nu este încă folosit.
            "is_used": False,
        },
        # =====================================================
        # TOKEN PENTRU GUEST
        # =====================================================
        {
            # Asociem token-ul utilizatorului "guest".
            "user": user_repository.get_instance_by_username("guest"),
            # Token-ul este deja folosit.
            "is_used": True,
        },
    ]
