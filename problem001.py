#!/usr/bin/env python
"""Find the sum of all the multiples of 3 or 5 below 1000"""

def multiple_sum(base, limit):
    """Returns the sum of all multiples of base less than max"""
    mult = base
    total = 0
    while mult < limit:
        total += mult
        mult += base
    return total

print  multiple_sum(3, 1000) + multiple_sum(5, 1000) - multiple_sum(15, 1000)
