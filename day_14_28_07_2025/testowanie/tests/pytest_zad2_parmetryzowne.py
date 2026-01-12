# TDD  - Test-Driven Development - czyli programowanie sterowane testami
# Jest to technika tworzenia oprogramowania,
# w której testy jednostkowe są pisane przed napisaniem kodu implementacyjnego

import pytest


def calculate_square(num):
    return num ** 2


def test_squre_1():
    assert calculate_square(2) == 4


# test parametryzowany
# uruchomiony wielokrotnie z róznymi argumentami

@pytest.mark.parametrize("input, expected_output", [(2, 4), (3, 9), (4, 16)])
def test_square_calculate_parametrized(input, expected_output):
    assert calculate_square(input) == expected_output
# pytest_zad2_parmetryzowne.py::test_squre_1 PASSED                                                                                             [ 25%]
# pytest_zad2_parmetryzowne.py::test_square_calculate_parametrized[2-4] PASSED                                                                  [ 50%]
# pytest_zad2_parmetryzowne.py::test_square_calculate_parametrized[3-9] PASSED                                                                  [ 75%]
# pytest_zad2_parmetryzowne.py::test_square_calculate_parametrized[4-16] PASSED                                                                 [100%]
