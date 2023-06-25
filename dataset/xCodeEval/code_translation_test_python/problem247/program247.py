def program247():
    a,b,c,d=map(int,input().split())
    count=0
    counter=0
    m=min(a,min(c,d))
    n=min(a-m,b)
    count=n*32
    counter=m*256
    print(count+counter)