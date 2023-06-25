def program3487():
    n,k=[int(i) for i in input().split()]
    a=[int(i) for i in input().split()]
    c=0
    day=0
    for i in range(n):
        c+=a[i]
        if(k>0):
            day+=1
            if(c>8):
                k-=8
                c-=8
            else:
                k-=c
                c=0
        else:
            break
    if(k<=0):
        print(day)
    else:
        print('-1')