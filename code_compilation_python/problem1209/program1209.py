    %%timeit
    n = int(input())
    b = 1
def get2(n):
        lis = []
        while(n>0):
            s=1
            i=0
            while(s*2<=n):
                s*=2
                i+=1
            lis.append(i)
            n-=s
        return lis
    li = get2(n)
    d = 1
    for i in li:
        t = 8
        for j in xrange(i):
            t = (t*t)%10
        d = (d*t)%10
    print d