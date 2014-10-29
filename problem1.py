#!/usr/bin/env python
"""Find the sum of all the multiples of 3 or 5 below 1000"""

def multiple_sum ( n, m ):
    num = n
    sum = 0
    while num < m:
        sum += num
        num += n
    return sum

print  multiple_sum(3, 1000) + multiple_sum(5, 1000) - multiple_sum(15,1000)
