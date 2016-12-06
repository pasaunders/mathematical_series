"""This file will test functions to generate Fibonacci and Lucas numbers."""

import pytest


PARAMS_TABLE_FIBONACCHI = [
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 3],
    [6, 5],
    [7, 8],
    [8, 13],
]


PARAMS_TABLE_LUCAS = []


@pytest.mark.parametrize("n, result", PARAMS_TABLE_FIBONACCHI)
def test_fibonacchi(n, result):
    """M and N should add up to result to create a fibbonachi sequence."""
    from series import fibonacci
    assert fibonacci(n) == result
