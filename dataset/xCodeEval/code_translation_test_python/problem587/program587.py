    import sys,math
    from math import factorial as fact
    from collections import defaultdict as dd
    input = lambda: sys.stdin.readline().strip()
    inp = lambda: list(map(int,input().split()))
    mod = 10**9+7
    #---------------------------------------------------
def C(n,r):
        if r>n:
            return 0
        return fact(n)//(fact(n-r)*fact(r))
def P(n,r):
        # if n==0:
        #     return 0
        if r>n:
            return 0
        return fact(n)//fact(n-r)
    # for _ in range(int(input())):
    n , x, pos = inp()
    a = [i for i in range(n)]
    g = 0
    l = 0
def bins(a,x,n):
        global g,l
        left = 0
        right = n
        while (left<right):
            mid = (left+right)//2
            if a[mid]==x:
                left = mid+1
            elif a[mid]<x:
                left = mid+1
                l+=1
            else:
                right = mid
                g+=1
        if left>0 and a[left-1]==x:
            return
        else:
            return
    bins(a,pos,n)
    dc = n-g-l-1
    actg = n-x
    actl = x-1
    # print(g,l,actl,actg,dc)
    # print(dc)
    ans = P(actg,g)*P(actl,l)*P(n-g-l-1,dc)
    print(ans%mod)