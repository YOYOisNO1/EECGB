def program691():
    import math
    n,m=input().split()
    n,m=[int(n),int(m)]
    a=[int(i) for i in input().split()]
    ma=max(a)
    if (m-ma)>=0:
        print(n)
    else:
        last=ma
        d1=0
        for i in range(0,n):
            if (m-a[i])<0:
                d=math.ceil(a[i]/m)
                if d>=d1:
                    d1=d
                    last=i
        print(last+1)