def program2362():
    n,m,a,b = map(int,input().split())
    nBuild = m-n%m
    nDem = n%m
    print(min(nBuild*a,nDem*b))