def program3615():
    from collections import*
    n,m=map(int,input().split())
    c=Counter(i*i%m for i in range(1,n+1))
    print(sum(c[k]*c[(m-k)%m]for k in c))