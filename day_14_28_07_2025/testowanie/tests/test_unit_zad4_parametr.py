import unittest


def divide(a, b):
    if b == 0:
        raise ValueError("Dzielenie prze zero")
    return a / b


class TestDivide(unittest.TestCase):
    def test_divide_ok(self):
        cases = [
            (10, 2, 5),
            (9, 3, 3),
            (-10, 2, -5)
        ]
        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                self.assertEqual(divide(a, b), expected)

    def test_divide_by_zero(self):
        for a, b in [(5, 0), (0, 0)]:
            with self.subTest(a=a, b=b):
                with self.assertRaises(ValueError):
                    divide(a, b)
# tests/test_unit_zad4_parametr.py::TestDivide::test_divide_by_zero
# tests/test_unit_zad4_parametr.py::TestDivide::test_divide_by_zero PASSED                                                                      [ 90%]
# tests/test_unit_zad4_parametr.py::TestDivide::test_divide_ok
# tests/test_unit_zad4_parametr.py::TestDivide::test_divide_ok PASSED
