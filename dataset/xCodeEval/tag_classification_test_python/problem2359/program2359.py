def program2359():
    n,m,a,b = map(int,input().split())
    if n%m == 0:
        ans = 0
    else:
        p = n//m
        ans = min(a*((p+1)*m-n),b*(n-p*m))
    print(ans)