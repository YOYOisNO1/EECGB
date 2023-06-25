def program2361():
    n,m,a,b=[int(x) for x in input().split()]
    print(min((n%m)*b,(m-n%m)*a))