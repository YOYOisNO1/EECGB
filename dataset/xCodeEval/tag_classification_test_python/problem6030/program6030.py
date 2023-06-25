def program6030():
    a,b=map(int,input().split())
    m=-1
    for i in range(70):
        if (a&(2**i)) ^ (b&(2**i)):
                m=i
    m+=1
    r=2**m
    r-=1
    print(r)