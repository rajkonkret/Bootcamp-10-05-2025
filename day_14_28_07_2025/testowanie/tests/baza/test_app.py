import pytest
from unittest.mock import patch
from app import get_user_email


def test_get_user_email_ok():
    fake_user = {
        "id": 1,
        "email": "mock@test.pl"
    }

    with patch("app.get_user_from_db") as mock_db:
        mock_db.return_value = fake_user

        result = get_user_email(1)

        assert result == "mock@test.pl"
        mock_db.assert_called_once_with(1)


def test_get_user_email_not_found():
    with patch("app.get_user_from_db") as mock_db:
        mock_db.return_value = None

        with pytest.raises(ValueError):
            get_user_email(999)