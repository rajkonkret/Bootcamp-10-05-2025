import fun_transactions as ft


def test_map_transactions_usd():
    result = [1000, 200, 500, 300, 700, 0, 0]
    assert ft.map_transactions(ft.transactions, "USD") == result
    # test_fun_transactions.py::test_map_transactions_usd PASSED


# test_reduce
def test_reduce_transactions():
    assert ft.reduce_transactions([1000, 500, 700, 0]) == 2200
    # test_fun_transactions.py::test_reduce_transactions PASSED


def test_filter_transactions_income():
    expected_list = [
        {"id": 1, "type": "income", "amount": 1000, "currency": "USD"},
        {"id": 3, "type": "income", "amount": 500, "currency": "USD"},
        {"id": 5, "type": "income", "amount": 700, "currency": "USD"},
        {"id": 7, "type": "income", "amount": 100, "currency": "EUR"},
    ]

    assert ft.filter_transactions(ft.transactions, "income") == expected_list
    # test_fun_transactions.py::test_filter_transactions_income PASSED


def test_process_transactions_expense_eur():
    assert ft.process_transactions(ft.transactions, "expense", "EUR") == 400


# (.venv) radoslawjaniak@mac transactions_zad % pytest -v
# ================================================================ test session starts ================================================================
# platform darwin -- Python 3.13.7, pytest-9.0.2, pluggy-1.6.0 -- /Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/.venv/bin/python
# cachedir: .pytest_cache
# rootdir: /Users/radoslawjaniak/PycharmProjects/BootCamp-11-10-2025A/day_14_11_01_2026/testowanie/transactions_zad
# plugins: anyio-4.12.0
# collected 4 items
#
# test_fun_transactions.py::test_map_transactions_usd PASSED                                                                                    [ 25%]
# test_fun_transactions.py::test_reduce_transactions PASSED                                                                                     [ 50%]
# test_fun_transactions.py::test_filter_transactions_income PASSED                                                                              [ 75%]
# test_fun_transactions.py::test_process_transactions_expense_eur PASSED                                                                        [100%]
#
# ================================================================= 4 passed in 0.02s =================================================================
# (.venv) radoslawjaniak@mac transactions_zad %


# ---------------------------------------------------------------------------
# testy zaproponowane przez AI
def test_filter_transactions_no_match():
    result = ft.filter_transactions(ft.transactions, "transfer")
    assert result == []
    # test_fun_transactions.py::test_filter_transactions_no_match PASSED


def test_filter_transactions_empty_input():
    assert ft.filter_transactions([], "income") == []
    # test_fun_transactions.py::test_filter_transactions_empty_input PASSED


def test_map_transactions_eur():
    input_data = [
        {"amount": 50, "currency": "EUR"},
        {"amount": 75, "currency": "EUR"},
    ]
    result = ft.map_transactions(input_data, "EUR")
    assert result == [50, 75]
    # test_fun_transactions.py::test_map_transactions_eur PASSED


def test_map_transactions_empty():
    assert ft.map_transactions([], "USD") == []
    # test_fun_transactions.py::test_map_transactions_empty PASSED


def test_process_transactions_income_eur():
    result = ft.process_transactions(ft.transactions, "income", "EUR")
    assert result == 100
    # test_fun_transactions.py::test_process_transactions_income_eur PASSED


def test_process_transactions_no_results():
    result = ft.process_transactions(ft.transactions, "transfer", "USD")
    assert result == 0
    # test_fun_transactions.py::test_process_transactions_no_results PASSED


def test_process_transactions_empty():
    result = ft.process_transactions([], "income", "USD")
    assert result == 0
