def count(b,n):
        a = [0]*(n+1)
        m = len(b)
        a[0]=1
        for i in range(1,n+1):
            for j in range(m):
                if(i>=b[j]):
                    a[i]+=a[i-b[j]]
        return a[n]
    n,k,d = list(map(int,input().split()))
    a = [i for i in range(1,k+1)]
    b = [i for i in range(1,d)]
    print((count(a,n)-count(b,n))%(10**9+7))