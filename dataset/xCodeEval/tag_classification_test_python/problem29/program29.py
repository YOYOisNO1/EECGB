def program29():
    n,k,t=map(int,input().split())
    if t<=k:
         print(t)
    elif t>k and t<=n:
         print(k)
    elif t>n:
         t=t-n
         print(k-t)
         