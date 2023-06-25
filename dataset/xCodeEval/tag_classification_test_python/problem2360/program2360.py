def program2360():
    n,m,a,b=map(int,input().split())
    print(min((n%m)*b,(m-(n%m))*a))