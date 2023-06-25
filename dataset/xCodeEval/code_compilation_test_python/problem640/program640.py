def program640():
    [n,a,b,c]=[int(x) for x in input().split()]
    k=0
    minprice=0
    for i in range (4):
        if (n+i)%4==0:
            k=i
    if k==0:
        print(0)
    elif k==1:
        print(min(a,b+c,3*c)
    elif k==2:
        print(min(b,2*a,2*c)
    elif k==3:
        print(min(c,3*a,b+a))