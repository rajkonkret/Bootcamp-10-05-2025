import unittest


def divide(a, b):
    return a / b


class TestDivide(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
# platform darwin -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0 -- /Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/day_14_11_01_2026/testowanie
# plugins: anyio-4.12.0
# collected 3 items
#
# tests/test_unit_zad1.py::MyTestCase::test_something FAILED                                                                                    [ 33%]
# tests/test_unit_zad2.py::TestDivide::test_divide PASSED                                                                                       [ 66%]
# tests/test_unit_zad2.py::TestDivide::test_divide_by_zero PASSED                                                                               [100%]
#
# ===================================================================== FAILURES ======================================================================
# _____________________________________________________________ MyTestCase.test_something _____________________________________________________________
#
# self = <testowanie.tests.test_unit_zad1.MyTestCase testMethod=test_something>
#
#     def test_something(self):
# >       self.assertEqual(True, False)
# E       AssertionError: True != False
#
# tests/test_unit_zad1.py:13: AssertionError
# ============================================================== short test summary info ==============================================================
# FAILED tests/test_unit_zad1.py::MyTestCase::test_something - AssertionError: True != False
# ============================================================ 1 failed, 2 passed in 0.05s ============================================================
# (.venv) radoslawjaniak@mac testowanie %
