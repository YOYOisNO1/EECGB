def program3815():
    I=lambda:map(int,input().split())
    n,d=I()
    a=sorted(I())+[-d]*99
    print(sum(a[:next(I())]))