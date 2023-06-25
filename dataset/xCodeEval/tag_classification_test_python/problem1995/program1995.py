    import sys
    sys.setrecursionlimit(999999999)
def solve(n,k,d,flag):
        if (n,k,d,flag) in dp:
            return dp[(n,k,d,flag)]
        if n==0:
            if flag:
                dp[(n,k,d,flag)]=1
            else:
                dp[(n,k,d,flag)]=0
        else:
            dp[(n,k,d,flag)]=0
            if flag:
                for i in xrange(1,k+1):
                    if n-i>=0:
                        dp[(n,k,d,flag)]+=solve(n-i,k,d,flag)
            else:
                for i in xrange(1,d):
                    if n-i>=0:
                        dp[(n,k,d,flag)]+=solve(n-i,k,d,False)
                for i in xrange(d,k+1):
                    if n-i>=0:
                        dp[(n,k,d,flag)]+=solve(n-i,k,d,True)
        return dp[(n,k,d,flag)]
    n,k,d=map(int,input().split())
    dp={}
    print(solve(n,k,d,False)%1000000007)