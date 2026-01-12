from unittest import TestCase


class TryTesting(TestCase):
    def test_always_passed(self):
        self.assertTrue(True)

    def test_uppercase(self):
        # sprawdzenie wyniku działania funkcji upper()
        assert 'python'.upper() == 'PYTHON'

    def test_reversed(self):
        assert list(reversed([1, 2, 3])) == [3, 2, 1]

    def test_reversed_test_case_style(self):
        self.assertEqual(
            list(reversed([1, 2, 3])),
            [3, 2, 1],
            "Odwrócenie listy [1,2,3], powinno dać [3,2,1]"
        )

    def test_always_fail(self):
        self.assertTrue(False, "Ten test celowo nie przejdzie")

# self = <testowanie.tests.test_unit_zad3.TryTesting testMethod=test_always_fail>
#
#     def test_always_fail(self):
# >       self.assertTrue(False, "Ten test celowo nie przejdzie")
# E       AssertionError: False is not true : Ten test celowo nie przejdzie
#
# tests/test_unit_zad3.py:23: AssertionError
