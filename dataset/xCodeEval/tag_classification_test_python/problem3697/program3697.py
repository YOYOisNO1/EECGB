def program3697():
    import math
    import os
    import random
    import re
    import sys
    from operator import itemgetter, attrgetter
    
    if __name__ == '__main__':
        n, k = list(map(int, input().strip().split()))
        a = list(map(int, input().strip().split()))
        b, p, s = list(), 0, ""
    
        for i in range(n):
            b.append((i + 1, a[i]))
        b.sort(key=itemgetter(1))
    
        while(p < n and k - b[p][1] >= 0):
            k -= b[p][1]
            p += 1
    
        print(p)
        for x in range(p):
            s += str(b[x][0])
            s += " "
        print(s.lstrip())