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


PARAMS_TABLE_SUM = [
    [1, 0, 1, 0],
    [2, 0, 1, 1],
    [3, 0, 1, 1],
    [4, 0, 1, 2],
    [5, 0, 1, 3],
    [6, 0, 1, 5],
    [7, 0, 1, 8],
    [8, 0, 1, 13],
    [1, 2, 1, 2],
    [2, 2, 1, 1],
    [3, 2, 1, 3],
    [4, 2, 1, 4],
    [5, 2, 1, 7],
    [6, 2, 1, 11],
    [7, 2, 1, 18],
    [8, 2, 1, 29],
]


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
    """Running function returns fibonacci sequence starting at n."""
    from series import sum_series
    assert sum_series(n, m, o) == result
