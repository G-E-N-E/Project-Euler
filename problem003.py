#!/usr/bin/env python
"""Problem 3 from Project Euler"""

def lpf(limit):
    """Returns the largest prime factor of limit"""

    multiple = 2
    largest = 1
    while 1:
        if limit % multiple == 0:
            limit = limit / multiple
            if multiple > lpf:
                largest = multiple
            if limit == 1:
                break
            multiple = 2
        else:
            multiple += 1
    return largest

print lpf(600851475143)
