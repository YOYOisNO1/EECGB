def readInts():
        return map(long, input().split())
def readInt():
        return long(input())
    import collections
    n,a,b = readInts()
    a,b = min(a,b), max(a,b)
    st, en = 1, n
    rC = 0
    r = 0
    N = n
    while N > 1:
        N/=2
        rC+=1
    while n > 0:
        n/=2
        
        mid = st + n - 1
        if a <= mid and b > mid:
            break
        if a > mid:
            st = mid + 1
        elif b <= mid:
            en = mid
        r+=1
    
    print("Final!") if 0 == r else rC - r
    #for i in xrange(n):