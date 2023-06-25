def program2650():
    l=lambda:map(int,input().split())
    a,b=l()
    c=0
    while a%b<>0:
        c+=a/b
        t=a%b
        a=b
        b=t
    print(c+a/b)