def program3372():
    a,m=map(int,input().split())
    i=f=0
    while True:
        if a%m==0:
            f=1
            break
        else:
            a+=a%m
            i+=1
        if i>25:
            break
    if f:
        print("Yes")
    else:
        print("No")