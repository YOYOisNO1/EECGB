def hcf(x, y):
    a,b,n=[int(i) for i in input().split()]
    for i in range(101):
        if i%2==0:
            n-=hcf(a,n)
            if n<=0:
               print(0)
               break
        else:
            n-=hcf(b,n)
            if n<=0:
               print(1)
               break