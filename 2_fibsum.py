#!/usr/bin/env python
"""Sum all even fibonacci number less than or equal to four million"""

r5 = 5**(0.5)
gr = (1 + r5) / 2

def fib( n ):
    return round((gr**n)/r5)

def problem2( limit ):
    n = 6
    sum = 2
    while True:
        fn = fib( n )
        if ( fn <= limit ):
            sum += fn
            n += 3
        else:
            break
    return sum

print problem2( 4000000 )
