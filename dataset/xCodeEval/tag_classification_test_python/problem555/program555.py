def program555():
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=0
    e=b
    for i in c:
        if e>=i:
            e-=i
        else:
            e=b-i
            d+=1
    print(d+1)