def program23():
    from math import ceil as cs
    n,k=map(int,input().split())
    r,g,b=2*n,5*n,8*n
    print(cs(r/k)+cs(g/k)+cs(b/k))