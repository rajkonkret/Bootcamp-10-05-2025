import pytest


# pip install pytest

#  pytest pytest_zad1.py -v - bogatsze informacje
def add(a, b):
    return a + b


print(add(3, 5))  # 8


# sprawdzenie funkcji add()
def test_addition():
    result = add(2.5, 3.5)
    assert result == 6
    assert result == 6.0


# dopisac funkcję divide()
# dopisac test do tej funkcji test_division()

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero!")
    return a / b


def test_division():
    assert divide(5, 1) == 5
    assert divide(5, 1) == 5.0


def test_division_by_two():
    assert divide(6, 2) == 3
    assert divide(6, 2) == 3.0


# sprawdzenie czy funkcja rzuci prawidłowy wyjątek w sytuacji gdy b=0
def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# def test_division_type():
#     assert divide(6, "2")  # TypeError
#
# prawidłowe podejscie do testowania wyjątków
def test_division_type_error():
    with pytest.raises(TypeError):
        divide(10, "2")

# pytest_zad1.py::test_addition PASSED                                                                                                          [ 20%]
# pytest_zad1.py::test_division PASSED                                                                                                          [ 40%]
# pytest_zad1.py::test_division_by_two PASSED                                                                                                   [ 60%]
# pytest_zad1.py::test_division_by_zero PASSED                                                                                                  [ 80%]
# pytest_zad1.py::test_division_type_error PASSED                                                                                               [100%]
#
# ================================================================= 5 passed in 0.01s =================================================================
