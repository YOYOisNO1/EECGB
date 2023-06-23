    import sys
    sys.setrecursionlimit(1000000)
def f(i,j):
        if j==n+1:
            return True
        if dp1[i][j]!=-1:
            return dp1[i][j]
        else:
            s=set()
            for i1 in range(i,i+2*k):
                if dp[(i1)%(2*k)][j]>l:
                    break
                if dp[(i1+1)%(2*k)][j+1]<=l:
                    s.add(f((i1+1)%(2*k),j+1))
            if True in s:
                dp1[i][j]=True
                return True
            dp1[i][j]=False
            return False
    for _ in range(int(input())):
        global l,k,n
        n,k,l=map(int,input().split())
        a=[int(o) for o in input().split()]
        dp=[[0 for i in range(n+2)]for j in range(2*k)]
        dp1=[[-1 for i in range(n+2)]for j in range(2*k)]
        for i in range(n):
            dp[0][i+1]=a[i]
            for j in range(2*k):
                if j<=k:
                    dp[j][i+1]=a[i]+j
                else:
                    dp[j][i+1]=a[i]+(k)-(j-k)
        print("Yes" if f(0,0) else "No")
        