def program4155():
    import math
    n , m = map(int,input().split())
    k  = n+m
    c = int(math.sqrt(k))
    a = int(math.sqrt(n))
    b = int(math.sqrt(m))
    ma = k
    ans=0
    for i in range(1,c+1):
        if i<=a and n%i==0:
            ma = min(ma,n//i)
        if i<=b and m%i==0:
            ma = min(ma,m//i)
        if k%i==0:
            t = k//i
            if t>=ma:
                ans = (i+t)*2
    print(ans)        