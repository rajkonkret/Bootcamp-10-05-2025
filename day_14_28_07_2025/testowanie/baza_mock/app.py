def get_user_from_db(user_id: int):
    """
    symulacja dostępu do bazy
    :param user_id:
    :return:
    """

    fake_db = {
        1: {"id": 1, "email": "jan@wp.pl"},
        2: {"id": 2, "email": "olo@wp.pl"}
    }

    return fake_db.get(user_id)


def get_user_email(user_id: int) -> str:
    user = get_user_from_db(user_id)

    if user is None:
        raise ValueError("User not found")

    return user["email"]
