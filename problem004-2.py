#!/usr/bin/env python
"""Problem 4 from Project Euler"""


def l_p():
    for a in xrange(9, 0, -1):
        for b in xrange(9, 0, -1):
            for c in xrange(9, 0, -1):
                i = int(str(a)+str(b)+str(c)+str(c)+str(b)+str(a))
                for j in xrange(999,100,-1):
                    if(i % j == 0  and i / j >= 100 and i / j < 999):
                        return i

print l_p()
