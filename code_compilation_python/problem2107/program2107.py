def program2107():
    f = lambda: (map (int,input().split()))
    n,A,B,C,T=f()
    print(sum(  A+max(0,(C-B))*(T-x)  for x in f() )