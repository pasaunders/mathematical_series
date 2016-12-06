"""This module calculates Fibonacci and Lucas sequences."""


def fibonacci(n):
    """This series returns the nth number of a Fibonacci sequence"""
    series = []
    for i in range(n):
        if i == 0 or i == 1:
            series.append(i)
        else:
            next_num = (i - 2) + (i - 1)
            series.append(next_num)
    return series[-1]
