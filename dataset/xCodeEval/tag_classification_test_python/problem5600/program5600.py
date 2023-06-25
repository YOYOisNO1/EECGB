def program5600():
    n,m = map(int,input().split())
    
    if n < m:
        n,m = m,n
    
    if m == 1:
        print(n)
    elif m == 2:
        print(2*(2*(n/4)) + min(n%4,2))
    else:
        print((n*m+1)/2)