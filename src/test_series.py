"""This file will test functions to generate Fibonacci and Lucas numbers."""

import pytest


PARAMS_TABLE_FIBONACCI = [
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 3],
    [6, 5],
    [7, 8],
    [8, 13],
]


PARAMS_TABLE_LUCAS = [
    [1, 2],
    [2, 1],
    [3, 3],
    [4, 4],
    [5, 7],
    [6, 11],
    [7, 18],
    [8, 29],
]


PARAMS_TABLE_SUM = []


@pytest.mark.parametrize("n, result", PARAMS_TABLE_FIBONACCI)
def test_fibonacci(n, result):
    """Running function fibonacci(n) should equal result."""
    from series import fibonacci
    assert fibonacci(n) == result


@pytest.mark.parametrize("n, result", PARAMS_TABLE_LUCAS)
def test_lucas(n, result):
    """Running function lucas(n) should equal result."""
    from series import lucas
    assert lucas(n) == result


@pytest.mark.parametrize("n, m, o, result", PARAMS_TABLE_SUM)
def test_sum(n, m, o, result):
    """Running function returns fibonacci sequence starting at n"""
