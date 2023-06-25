def program405():
    n,a,b,c=map(int, input().split())
    a,b,c=sorted([a,b,c])
    r=[]
    for i in range(n/a,-1,-1):
        for j in range((n-i*a)/b,-1,-1):
            d=n-i*a-j*b
            if not d%c:
                r.append(i + j + d/c)
        if r and r[-1] == n/a:
            break
    print(sorted(r,) reverse=True)[0]