def program315():
    from __future__ import division
    import math
    __author__ = 'MoustaphaSaad'
    n = int(input())
    res = n/2
    upre = math.ceil(res)
    if res != upre:
        print(int(-upre))
    else:
        print(int(upre))