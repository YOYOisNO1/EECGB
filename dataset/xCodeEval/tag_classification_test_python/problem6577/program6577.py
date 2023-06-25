def program6577():
    from math import *
    n,r1,r2=map(int, input().split())
    print('YES') if ((n < 2 and r2 <= r1) or (r2 <= (r1 - r2) and (asin(r2 / float(r1 - r2)) * n <= (acos(-1.0) + 1.0e-9)))) else 'NO'