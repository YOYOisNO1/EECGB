def program2323():
    n,m=map(int,input().split())
    print(min(m,n),(max(m,n)-min(n,m))//2)