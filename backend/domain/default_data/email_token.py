from api.repository import UserRepository


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
