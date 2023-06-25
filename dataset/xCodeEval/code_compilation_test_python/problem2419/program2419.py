def program2419():
    a,b,c,d=map(int,input().split()))
    s=0
    p=min(a,c,d)
    s+=p*256
    a-=p
    q=min(b,a)
    s+=32*q
    print(s)