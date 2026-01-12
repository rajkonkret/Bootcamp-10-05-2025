import pytest


def divide(a, b):
    return a / b


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (10, 2, 5),
        (9, 3, 3),
        (12, 4, 3),
    ]
)
def test_divide_ok(a, b, expected):
    assert divide(a, b) == expected


# pytest_zad3_param2.py::test_divide_ok[10-2-5] PASSED                                                                                          [ 33%]
# pytest_zad3_param2.py::test_divide_ok[9-3-3] PASSED                                                                                           [ 66%]
# pytest_zad3_param2.py::test_divide_ok[12-4-3] PASSED                                                                                          [100%]

@pytest.mark.parametrize("a,b",
                         [
                             (1, 0),
                             (5, 0),
                             (7, 0),
                             # (7,1)
                         ]
                         )
def test_divide_raises_zerodivisionerror(a, b):
    with pytest.raises(ZeroDivisionError):
        divide(a, b)
# pytest_zad3_param2.py::test_divide_raises_zerodivisionerror[1-0] PASSED                                                                       [ 57%]
# pytest_zad3_param2.py::test_divide_raises_zerodivisionerror[5-0] PASSED                                                                       [ 71%]
# pytest_zad3_param2.py::test_divide_raises_zerodivisionerror[7-0] PASSED                                                                       [ 85%]
# pytest_zad3_param2.py::test_divide_raises_zerodivisionerror[7-1] FAILED                                                                       [100%]
