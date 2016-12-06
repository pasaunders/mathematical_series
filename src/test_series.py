"""This file will test functions to generate Fibonacci and Lucas numbers."""

import pytest


PARAMS_TABLE_FIBONACCHI = [
    # [0, 0, 0],
    # [0, 0, 1],
    [0, 1, 1],
    [1, 1, 2],
    [1, 2, 3],
    [2, 3, 5],
    [3, 5, 8],
    [5, 8, 13],
]


PARAMS_TABLE_LUCAS = []


@pytest.mark.parametrize("m, n, result", PARAMS_TABLE_FIBONACCHI)
def test_fibonacchi(m, n, result):
    """M and N should add up to result to create a fibbonachi sequence."""
    assert m + n == result
