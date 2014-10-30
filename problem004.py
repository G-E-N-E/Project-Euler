#!/usr/bin/env python
"""Problem 4 from Project Euler"""


def is_palin(num):
    """Returns True if num is palindromic, else False"""

    num_str = str(num)
    rev_str = num_str[::-1]

    if num_str == rev_str:
        return True
    return False


LOW = 100
HIGH = 1000
largest = 0

for i in xrange(LOW, HIGH):
    for j in xrange(LOW, HIGH):
        number = i * j
        if is_palin(number) and number > largest:
            largest = number

print largest

