def program2719():
    r=lambda:map(int,input().split())
    n,m,k=r()
    if k>n+m-2:
        print(-1)
        exit()
    if n>m:
        n,m=m,n
    if k<n:
        print(max((n/(k+1))*m,) (m/(k+1))*n)
    elif k<m:
        print(max(m/(k+2-n),) n*(m/(k+1)))
    else:
        print(max(m/(k+2-n),) n/(k+2-m))