    import sys
    sys.setrecursionlimit(10000)
    
    D = {(1,0):1,(1,1):0}
    n,m,k = [int(x) for x in input().split()]
    
def f(n,k):
        if k == 0:
            return m
        if k >= n:
            return 0
        if (n,k) in D:
            return D[(n,k)]
        else:
            ans = (f(n-1,k)+(m-1)*f(n-1,k-1))%998244353
            D[(n,k)] = ans
            return ans
            
    print(f(n,k))