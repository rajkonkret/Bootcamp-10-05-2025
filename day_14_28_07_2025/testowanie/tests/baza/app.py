def get_user_from_db(user_id: int):
    """
    Symulacja dostępu do bazy danych
    """
    print(">>> Łączenie z bazą danych...")

    fake_db = {
        1: {"id": 1, "email": "jan@test.pl"},
        2: {"id": 2, "email": "ola@test.pl"},
    }

    return fake_db.get(user_id)


def get_user_email(user_id: int) -> str:
    user = get_user_from_db(user_id)

    if user is None:
        raise ValueError("User not found")

    return user["email"]