def program1335():
    m,n=map(int,input().split())
    c=int(n/2)
    d=int(m/2)
    if n%2==0:
        print(c*m)
    else:
        print(c*m + d)