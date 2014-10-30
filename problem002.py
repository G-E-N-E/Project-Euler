#!/usr/bin/env python
"""Sum all even fibonacci number less than or equal to four million"""

R5 = 5**(0.5)
GR = (1 + R5) / 2

def fib(index):
    """Finds the fibonacci number at index"""
    return round((GR**index)/R5)

def problem2(limit):
    """Returns the sum of all even fibonacci numbers less than limit + 1"""
    index = 6
    total = 2
    while True:
        fib_n = fib(index)
        if fib_n <= limit:
            total += fib_n
            index += 3
        else:
            break
    return total

print problem2(4000000)
