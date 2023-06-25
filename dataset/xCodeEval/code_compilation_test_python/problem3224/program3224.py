    from __future__ import print_fucntion
    n = int(input())
def sqrt(i):
        global n
        x = i
        for rep in range(1, n-1):
            if x == 1: return 0
            x = x*i%n
        if x == 1: return 1
        return 0
    a = []
    for i in range(1,n):
        a[i] = sqrt(i)
    print(sum(a))