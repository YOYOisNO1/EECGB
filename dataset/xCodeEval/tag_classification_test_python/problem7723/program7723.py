def cc(n,s):
        p=(n-1)/s+1
        return p*(n-(p-1)*s)
    n,m,s=map(int,input().split())
    print(cc(n,s)*cc(m,s))