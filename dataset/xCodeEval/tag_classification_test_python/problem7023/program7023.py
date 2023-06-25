    from sys import stdin 
    n = int(stdin.readline())
    di = {}
    di[1] = 0 
    di[0] = 0 
    for po in xrange(1,66):
        x = 1<<(po -1)
        di[x] = (po)*x 
def get(n):
        if n in di:
            return di[n/2]
        i = 64 
        while i >=0:
            if n & (1<<i):
                break 
            i-=1 
        return di[1<<(i-1)] +  (1<<i) + get(n-(1<<i))
    print(get(n))