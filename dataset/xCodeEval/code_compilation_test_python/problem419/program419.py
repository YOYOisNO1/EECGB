def program419():
    import math
    t=1
    l=[1,1]
    for  i in range(2,100000):
            l.append((l[i-1]+l[i-2])998244353)
    while t:
            t-=1
            n=int(input())
            x=l[n-1]
            y=pow(2,n)
            print(x*pow(y,998244351,998244353)%998244353)
            