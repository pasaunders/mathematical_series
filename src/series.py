"""This module calculates Fibonacci and Lucas sequences."""


def fibonacci(n):
    """Return the nth number of a Fibonacci sequence."""
    series = []
    for i in range(n):
        if i == 0 or i == 1:
            series.append(i)
        else:
            next_num = (series[i - 2]) + (series[i - 1])
            series.append(next_num)
    return series[-1]


def lucas(n):
    """Return the nth number of a Lucas sequence."""
    series = []
    for i in range(n):
        if i == 0:
            series.append(2)
        elif i == 1:
            series.append(1)
        else:
            series.append(series[i - 2] + series[i - 1])
    return series[-1]


def sum_series(n, m=0, o=1):
    """Return a fibonacci sequence starting at n"""
    series = []
    for i in range(n):
        if i == 0:
            series.append(m)
        elif i == 1:
            series.append(o)
        else:
            series.append(series[i - 2] + series[i - 1])
    return series[-1]
