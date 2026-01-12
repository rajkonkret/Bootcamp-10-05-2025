# unittest - framwork do testów jednostkowych
# pytest  - uruchamia testy
# asercje - instrukcje sprawdzające poprawnośc założeń w kodzie
# pytest szuka plików/funkcji  z nazwą test_* lub *_test
# pytest pytest_zad3_param2.py -vvv
# pytest tests/ - katalog z testami, pliki spełniające warunek nazwy zostaną uruchomione

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
# ============================= test session starts ==============================
# collecting ... collected 1 item
#
# day_14_11_01_2026/testowanie/tests/test_unit_zad1.py::MyTestCase::test_something
#
# ============================== 1 failed in 0.02s ===============================
# FAILED [100%]
# day_14_11_01_2026/testowanie/tests/test_unit_zad1.py:10 (MyTestCase.test_something)
# False != True
#
# Expected :True
# Actual   :False
# <Click to see difference>
#
# self = <testowanie.tests.test_unit_zad1.MyTestCase testMethod=test_something>
#
#     def test_something(self):
# >       self.assertEqual(True, False)
#
# day_14_11_01_2026/testowanie/tests/test_unit_zad1.py:12: AssertionError
#
# Process finished with exit code 1
#     def test_something(self):
# >       self.assertEqual(True, False)
# E       AssertionError: True != False
