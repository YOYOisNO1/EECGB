def program2696():
    n,k=[int(i) for i in input().split()]
    if (n*2)%k==0:
        a=(n*2)//k
    else:
        a=(n*2)//k+1
    if (n*5)%k==0:
        a=a+(n*5)//k
    else:
        a=a+(n*5)//k+1
    if (n*8)%k==0:
        a=a+(n*8)//k
    else:
        a=a+(n*8)//k+1
    print(a)